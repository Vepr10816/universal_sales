import 'dart:io';

import 'package:conduit/conduit.dart';
import 'package:jaguar_jwt/jaguar_jwt.dart';

import '../model/role_user.dart';

///Ностройка токенов.
abstract class AppUtils {
  const AppUtils._();

  ///Получение первичного ключа пользователя из токена.
  static int getIdFromToken(String token) {
    try {
      final key = Platform.environment["SECRET_KEY"] ?? 'SECRET_KEY';
      final jwtCLaim = verifyJwtHS256Signature(token, key);
      return int.parse(jwtCLaim["id"].toString());
    } catch (e) {
      rethrow;
    }
  }

  ///Получение первичного ключа записи в БД из header.
  static int getIdFromHeader(String header) {
    try {
      final token = const AuthorizationBearerParser().parse(header);
      final id = getIdFromToken(token ?? "");
      return id;
    } catch (e) {
      rethrow;
    }
  }

  ///Проверка роли пользователя.
  static Future<bool> checkAdmin(String header, managedContext) async{
      final currentUserId = AppUtils.getIdFromHeader(header);

      final qGetRoleUser = Query<RoleUser>(managedContext)..where((element) => element.user!.id).equalTo(currentUserId)..where((x) => x.roles!.id).equalTo(1);

      final getRoleUser = await qGetRoleUser.fetchOne();

      if(getRoleUser == null) {
        return false;
      } else {
        return true;
      }
  }
}