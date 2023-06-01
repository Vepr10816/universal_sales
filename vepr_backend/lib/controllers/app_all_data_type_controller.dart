import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/data_type.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllDataTypeController extends ResourceController {
  AppAllDataTypeController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get()
  Future<Response> getFullDataType(
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetDataType = Query<DataType>(managedContext);

      final List<DataType> list = await qGetDataType.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одного типа данных"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}