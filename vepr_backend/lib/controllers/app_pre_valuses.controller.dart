import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/pre_values.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppPreValuesController extends ResourceController {
  AppPreValuesController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createPreValues(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() PreValues bodyPreValues
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreatePreValuesData = Query<PreValues>(managedContext)
        ..values.preValue = bodyPreValues.preValue
        ..values.characteristics!.id = bodyPreValues.idCharacteristics;

      await qCreatePreValuesData.insert();

      return AppResponse.ok(message: 'Успешное создание Предзаполненного значения');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Предзаполненного значения');
    }
  }

  @Operation.put('id')
  Future<Response> updatePreValues(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() PreValues bodyPreValues
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final characteristc = await managedContext.fetchObjectWithID<PreValues>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Предзаполненное значение не найдена");
      }
      final qUpdatePreValues = Query<PreValues>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.preValue = bodyPreValues.preValue
        ..values.characteristics!.id = bodyPreValues.idCharacteristics;
      await qUpdatePreValues.update();

      return AppResponse.ok(message: 'Предзаполненное значение обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getPreValuesFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final characteristc = await managedContext.fetchObjectWithID<PreValues>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Предзаполненное значение не найдена");
      }
      return Response.ok(characteristc);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Предзаполненного значения");
    }
  }


  @Operation.delete("id")
  Future<Response> deletePreValues(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final characteristc = await managedContext.fetchObjectWithID<PreValues>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Предзаполненное значение не найдена");
      }
      final qDeletePreValues = Query<PreValues>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeletePreValues.delete();
      return AppResponse.ok(message: "Успешное удаление Предзаполненного значения");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Предзаполненного значения");
    }
  }

}