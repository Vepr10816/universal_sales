import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/pre_values.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllPreValuesController extends ResourceController {
  AppAllPreValuesController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idCharacteristics")
  Future<Response> getFullPreValues(@Bind.path("idCharacteristics") int idCharacteristics,
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetPreValues = Query<PreValues>(managedContext)..where((x) => x.characteristics?.id).equalTo(idCharacteristics);

      final List<PreValues> list = await qGetPreValues.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], 
                                message: "У данной характеристики нет предзаполненных значений"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}