import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/requisites.dart';
import '../utils/app_response.dart';

class AppRequisitesController extends ResourceController {
  AppRequisitesController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createRequisites(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Requisites bodyRequisites
  ) async {
    try {

      final qCreateRequisitesData = Query<Requisites>(managedContext)
        ..values.requisitesName = bodyRequisites.requisitesName
        ..values.requisitesValue = bodyRequisites.requisitesValue
        ..values.mycompany!.id = bodyRequisites.idMycompany;

      await qCreateRequisitesData.insert();

      return AppResponse.ok(message: 'Успешное создание реквизита');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания реквизита');
    }
  }

  @Operation.put('id')
  Future<Response> updateRequisites(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Requisites bodyRequisites
  ) async {
    try {
      final requisite = await managedContext.fetchObjectWithID<Requisites>(id);
      if (requisite == null) {
        return AppResponse.ok(message: "реквизит не найден");
      }
      final qUpdateRequisites = Query<Requisites>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.requisitesName = bodyRequisites.requisitesName
        ..values.requisitesValue = bodyRequisites.requisitesValue
        ..values.mycompany!.id = bodyRequisites.idMycompany;

      await qUpdateRequisites.update();

      return AppResponse.ok(message: 'реквизит обновлен');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getRequisitesFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final requisite = await managedContext.fetchObjectWithID<Requisites>(id);
      if (requisite == null) {
        return AppResponse.ok(message: "Реквизит не найден");
      }
      return Response.ok(requisite);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения реквизита");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteRequisites(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final requisite = await managedContext.fetchObjectWithID<Requisites>(id);
      if (requisite == null) {
        return AppResponse.ok(message: "Реквизит не найден");
      }
      final qDeleteRequisites = Query<Requisites>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteRequisites.delete();
      return AppResponse.ok(message: "Успешное удаление Реквизита");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Реквизита");
    }
  }

}