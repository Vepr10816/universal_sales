import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/requisites.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllRequisitesController extends ResourceController {
  AppAllRequisitesController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idCompany")
  Future<Response> getFullRequisites(@Bind.path("idCompany") int idCompany) 
  async {
    try {

      final qGetRequisites = Query<Requisites>(managedContext)..where((x) => x.mycompany?.id).equalTo(idCompany);

      final List<Requisites> list = await qGetRequisites.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одного реквизита"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  /*


  @Operation.delete("id")
  Future<Response> deleteFinanceData(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final currentUserId = AppUtils.getIdFromHeader(header);
      final financeData = await managedContext.fetchObjectWithID<FinanceData>(id);
      if (financeData == null) {
        return AppResponse.ok(message: "Финансовая запись не найден");
      }
      if (financeData.user?.id != currentUserId) {
        return AppResponse.ok(message: "Нет доступа к финансовой записи :(");
      }
      final qDeleteFinanceData = Query<FinanceData>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteFinanceData.delete();
      return AppResponse.ok(message: "Успешное удаление финансовой записи");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления финансовой записи");
    }
  }*/

 
  


  

}