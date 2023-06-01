import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/characteristics.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppCharacteristicsController extends ResourceController {
  AppCharacteristicsController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createCharacteristics(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Characteristics bodyCharacteristics
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateCharacteristicsData = Query<Characteristics>(managedContext)
        ..values.characteristicName = bodyCharacteristics.characteristicName
        ..values.selectable = bodyCharacteristics.selectable
        ..values.datatype!.id = bodyCharacteristics.idDatatype
        ..values.subcategory!.id = bodyCharacteristics.idSubcategory;

      await qCreateCharacteristicsData.insert();

      return AppResponse.ok(message: 'Успешное создание Характеристики');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Характеристики');
    }
  }

  @Operation.put('id')
  Future<Response> updateCharacteristics(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Characteristics bodyCharacteristics
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final characteristc = await managedContext.fetchObjectWithID<Characteristics>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Характеристика не найдена");
      }
      final qUpdateCharacteristics = Query<Characteristics>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.characteristicName = bodyCharacteristics.characteristicName
        ..values.selectable = bodyCharacteristics.selectable
        ..values.datatype!.id = bodyCharacteristics.idDatatype
        ..values.subcategory!.id = bodyCharacteristics.idSubcategory;
      await qUpdateCharacteristics.update();

      return AppResponse.ok(message: 'Характеристика обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getCharacteristicsFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final qGetCharacteristic = Query<Characteristics>(managedContext)..join(object: (x) => x.datatype)..where((x) => x.id).equalTo(id);

      final Characteristics? characteristic = await qGetCharacteristic.fetchOne();
      if (characteristic == null) {
        return AppResponse.ok(message: "Характеристика не найдена");
      }
      return Response.ok(characteristic);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Характеристики");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteCharacteristics(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final characteristc = await managedContext.fetchObjectWithID<Characteristics>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Характеристика не найдена");
      }
      final qDeleteCharacteristics = Query<Characteristics>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteCharacteristics.delete();
      return AppResponse.ok(message: "Успешное удаление Характеристики");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Характеристики");
    }
  }

}