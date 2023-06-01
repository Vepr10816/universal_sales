import 'dart:developer';
import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/category.dart';
import '../model/response.dart';
import '../model/subcategory.dart';
import '../utils/app_response.dart';

class AppAllCategoryFromUserController extends ResourceController {
  AppAllCategoryFromUserController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idCompany")
  Future<Response> getFullCategory(@Bind.path("idCompany") int idCompany) 
  async {
    try {

      final qGetCategory = Query<Category>(managedContext)
      ..where((x) => x.mycompany?.id).equalTo(idCompany)
      ..join(set:(x) => x.subcategoryList);

      final List<Category> categoryList = await qGetCategory.fetch();

      for(var category in categoryList)
      {
        final qGetSubcategory = Query<Subcategory>(managedContext)
        ..where((x) => x.category?.id).equalTo(category.id)
        ..join(set: (x) => x.productList);

        final List<Subcategory> subcategoryList = await qGetSubcategory.fetch();
        
        for(var subcategory in subcategoryList)
        {
          if(subcategory.productList!.isEmpty)
          {
            category.subcategoryList?.removeWhere((element) => element.id == subcategory.id);
          }
        }
      }

      categoryList.removeWhere((element) => element.subcategoryList!.isEmpty);

      if (categoryList.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одной категории"));
      }

      return Response.ok(categoryList);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}