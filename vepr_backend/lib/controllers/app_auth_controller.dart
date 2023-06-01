import 'dart:io';

import 'package:conduit/conduit.dart';
import 'package:jaguar_jwt/jaguar_jwt.dart';
import 'package:vepr_backend/model/role_user.dart';

import '../model/response.dart';
import '../model/user.dart';
import '../utils/app_utils.dart';

class AppAuthContoller extends ResourceController {
  AppAuthContoller(this.managedContext);

  final ManagedContext managedContext;

  @Operation.get()
  Future<Response> getRoleandToken(@Bind.query('tgID') String tgID,) async {
    try{
      final qFindUser = Query<User>(managedContext)
        ..where((element) => element.tgId).equalTo(tgID)
        ..returningProperties(
          (element) => [
            element.refreshToken
          ],
        );
        final findUser = await qFindUser.fetchOne();
         return Response.ok(ModelResponse(
              data: findUser!.backing.contents,
              message: 'Успешное получение токена',
            ));

    } on QueryException catch (e) {
      return Response.serverError(body: ModelResponse(message: e.message));
    }

  }


  @Operation.put()
  Future<Response> signTg(@Bind.query('tgID') String tgID, @Bind.query('idRole') int idRole) async {
    
    final qFindUser = Query<User>(managedContext)
        ..where((element) => element.tgId).equalTo(tgID)
        ..returningProperties(
          (element) => [
            element.id
          ],
        );

      // получаем первый элемент из поиска
      final findUser = await qFindUser.fetchOne();

      if (findUser == null) {
        try {
          late final int id;

          // создаем транзакицю
          await managedContext.transaction((transaction) async {
            // Создаем запрос для создания пользователя
            final qCreateUser = Query<User>(transaction)
              ..values.tgId = tgID;

            // Добавление пользоваетля в базу данных
            final createdUser = await qCreateUser.insert();

            // Сохраняем id пользователя
            id = createdUser.id!;

            // Обновление токена
            _updateTokens(id, transaction);
          });

          // Получаем данные пользователя по id
          final userData = await managedContext.fetchObjectWithID<User>(id);

          final qCreateUser = Query<RoleUser>(managedContext)
          ..values.roles!.id = idRole
          ..values.user!.id = id;

          await qCreateUser.insert();

          return Response.ok(
            ModelResponse(
              data: userData!.backing.contents,
              message: 'Пользователь успешно зарегистрировался',
            ),
          );
        } on QueryException catch (e) {
          return Response.serverError(body: ModelResponse(message: e.message));
        }
      }
      else{
        try {
            // Получаем данные пользователя
            final newUser = await managedContext.fetchObjectWithID<User>(findUser.id);
            return Response.ok(ModelResponse(
              data: newUser!.backing.contents,
              message: 'Успешная авторизация',
            ));
        } on QueryException catch (e) {
          return Response.serverError(body: ModelResponse(message: e.message));
        }
      }
  }

  @Operation.post('refresh')
  Future<Response> refreshToken(
      @Bind.path('refresh') String refreshToken) async {
    try {
      // Полчаем id пользователя из jwt token
      final id = AppUtils.getIdFromToken(refreshToken);

      // Получаем данные пользователя по его id
      final user = await managedContext.fetchObjectWithID<User>(id);

      if (user!.refreshToken != refreshToken) {
        return Response.unauthorized(body: 'Token не валидный');
      }

      // Обновление token
      _updateTokens(id, managedContext);

      return Response.ok(
        ModelResponse(
          data: user.backing.contents,
          message: 'Токен успешно обновлен',
        ),
      );
    } on QueryException catch (e) {
      return Response.serverError(body: ModelResponse(message: e.message));
    }
  }

  void _updateTokens(int id, ManagedContext transaction) async {
    final Map<String, String> tokens = _getTokens(id);

    final qUpdateTokens = Query<User>(transaction)
      ..where((element) => element.id).equalTo(id)
      ..values.accessToken = tokens['access']
      ..values.refreshToken = tokens['refresh'];

    await qUpdateTokens.updateOne();
  }

  // Генерация jwt token
  Map<String, String> _getTokens(int id) {
    // todo remove when release
    final key = Platform.environment['SECRET_KEY'] ?? 'SECRET_KEY';
    final accessClaimSet = JwtClaim(
      maxAge: const Duration(hours: 1), // Время жизни token
      otherClaims: {'id': id},
    );
    final refreshClaimSet = JwtClaim(
      otherClaims: {'id': id},
    );
    final tokens = <String, String>{};
    tokens['access'] = issueJwtHS256(accessClaimSet, key);
    tokens['refresh'] = issueJwtHS256(refreshClaimSet, key);

    return tokens;
  }
}