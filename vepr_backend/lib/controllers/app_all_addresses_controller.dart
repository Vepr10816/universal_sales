import 'dart:io';
import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/addresses.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

//Контроллер получения всех адресов компании
class AppAllAddressesController extends ResourceController {
  AppAllAddressesController(this.managedContext);

  final ManagedContext managedContext;

  ///Get метод создания адреса.
  ///[idCompany] - уникальный идентификатор компании.
  @Operation.get("idCompany")
  Future<Response> getFullAddresses(@Bind.path("idCompany") int idCompany) 
  async {
    try {

      final qGetAddresses = Query<Addresses>(managedContext)..where((x) => x.mycompany?.id).equalTo(idCompany);

      final List<Addresses> list = await qGetAddresses.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одного адреса"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}