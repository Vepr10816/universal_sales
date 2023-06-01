import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/category.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppCategoryController extends ResourceController {
  AppCategoryController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createCategory(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Category bodyCategory
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateCategoryData = Query<Category>(managedContext)
        ..values.categoryName = bodyCategory.categoryName
        ..values.mycompany!.id = bodyCategory.idMycompany;

      await qCreateCategoryData.insert();

      return AppResponse.ok(message: 'Успешное создание категории');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания категории');
    }
  }

  @Operation.put('id')
  Future<Response> updateCategory(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Category bodyCategory
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final category = await managedContext.fetchObjectWithID<Category>(id);
      if (category == null) {
        return AppResponse.ok(message: "Категория не найдена");
      }
      final qUpdateCategory = Query<Category>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.categoryName = bodyCategory.categoryName
        ..values.mycompany!.id = bodyCategory.idMycompany;
      await qUpdateCategory.update();

      return AppResponse.ok(message: 'Категория обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getCategoryFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final category = await managedContext.fetchObjectWithID<Category>(id);
      if (category == null) {
        return AppResponse.ok(message: "Категория не найдена");
      }
      return Response.ok(category);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения категории");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteCategory(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final category = await managedContext.fetchObjectWithID<Category>(id);
      if (category == null) {
        return AppResponse.ok(message: "Категория не найдена");
      }
      final qDeleteCategory = Query<Category>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteCategory.delete();
      return AppResponse.ok(message: "Успешное удаление Категории");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Категории");
    }
  }

}