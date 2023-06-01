import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/response.dart';
import '../model/subcategory.dart';
import '../utils/app_response.dart';

class AppAllSubcategoryController extends ResourceController {
  AppAllSubcategoryController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idCategory")
  Future<Response> getFullSubcategory(@Bind.path("idCategory") int idCategory) 
  async {
    try {

      final qGetSubcategory = Query<Subcategory>(managedContext)
      ..where((x) => x.category?.id).equalTo(idCategory)
      ..join(set: (x) => x.productList)
      ..join(object: (x) => x.category);

      final List<Subcategory> list = await qGetSubcategory.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одной подкатегории"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}