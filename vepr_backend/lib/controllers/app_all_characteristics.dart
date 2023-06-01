import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/characteristics.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllCharacteristicsController extends ResourceController {
  AppAllCharacteristicsController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idSubcategory")
  Future<Response> getFullCharacteristics(@Bind.path("idSubcategory") int idSubcategory) 
  async {
    try {

      final qGetCharacteristics = Query<Characteristics>(managedContext)..where((x) => x.subcategory?.id).equalTo(idSubcategory)
      ..join(object: (x) => x.datatype)
      ..join(set: (x) => x.preValuesList);

      final List<Characteristics> list = await qGetCharacteristics.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "У данной подкатегории нет характеристик"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}