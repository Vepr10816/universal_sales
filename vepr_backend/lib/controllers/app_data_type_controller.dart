import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/data_type.dart';
import '../utils/app_response.dart';

class AppDataTypeController extends ResourceController {
  AppDataTypeController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.get("id")
  Future<Response> getDataTypeFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final category = await managedContext.fetchObjectWithID<DataType>(id);
      if (category == null) {
        return AppResponse.ok(message: "Тип данныъ не найден");
      }
      return Response.ok(category);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения типа данных");
    }
  }

}