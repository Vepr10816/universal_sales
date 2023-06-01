import 'dart:developer';
import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/category.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllCategoryController extends ResourceController {
  AppAllCategoryController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idCompany")
  Future<Response> getFullCategory(@Bind.path("idCompany") int idCompany) 
  async {
    try {

      final qGetCategory = Query<Category>(managedContext)
      ..where((x) => x.mycompany?.id).equalTo(idCompany)
      ..join(set:(x) => x.subcategoryList);

      final List<Category> list = await qGetCategory.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одной категории"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}