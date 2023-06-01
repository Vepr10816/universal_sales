import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/currency.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllCurrencyController extends ResourceController {
  AppAllCurrencyController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get()
  Future<Response> getFullCurrency(
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetCurrency = Query<Currency>(managedContext);

      final List<Currency> list = await qGetCurrency.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Валюты не заполнены"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}