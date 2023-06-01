import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/currency.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppCurrencyController extends ResourceController {
  AppCurrencyController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createCurrency(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Currency bodyCurrency
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateCurrencyData = Query<Currency>(managedContext)
        ..values.currencyName = bodyCurrency.currencyName;

      await qCreateCurrencyData.insert();

      return AppResponse.ok(message: 'Успешное создание Валюты');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Валюты');
    }
  }

  @Operation.put('id')
  Future<Response> updateCurrency(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Currency bodyCurrency
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final currensy = await managedContext.fetchObjectWithID<Currency>(id);
      if (currensy == null) {
        return AppResponse.ok(message: "Валюта не найдена");
      }
      final qUpdateCurrency = Query<Currency>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.currencyName = bodyCurrency.currencyName;
      await qUpdateCurrency.update();

      return AppResponse.ok(message: 'Валюта обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getCurrencyFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final currensy = await managedContext.fetchObjectWithID<Currency>(id);
      if (currensy == null) {
        return AppResponse.ok(message: "Валюта не найдена");
      }
      return Response.ok(currensy);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Валюты");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteCurrency(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final currensy = await managedContext.fetchObjectWithID<Currency>(id);
      if (currensy == null) {
        return AppResponse.ok(message: "Валюта не найдена");
      }
      final qDeleteCurrency = Query<Currency>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteCurrency.delete();
      return AppResponse.ok(message: "Успешное удаление Валюты");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Валюты");
    }
  }

}