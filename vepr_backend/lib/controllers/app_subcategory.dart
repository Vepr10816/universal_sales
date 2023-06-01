import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/subcategory.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppSubcategoryController extends ResourceController {
  AppSubcategoryController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createSubcategory(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Subcategory bodySubcategory
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateSubcategoryData = Query<Subcategory>(managedContext)
        ..values.subcategoryName = bodySubcategory.subcategoryName
        ..values.category!.id = bodySubcategory.idCategory;

      await qCreateSubcategoryData.insert();

      return AppResponse.ok(message: 'Успешное создание Подкатегории');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Подкатегории');
    }
  }

  @Operation.put('id')
  Future<Response> updateSubcategory(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Subcategory bodySubcategory
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final subcategory = await managedContext.fetchObjectWithID<Subcategory>(id);
      if (subcategory == null) {
        return AppResponse.ok(message: "Подкатегория не найдена");
      }
      final qUpdateSubcategory = Query<Subcategory>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.subcategoryName = bodySubcategory.subcategoryName
        ..values.category!.id = bodySubcategory.idCategory;
      await qUpdateSubcategory.update();

      return AppResponse.ok(message: 'Подкатегория обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getSubcategoryFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final subcategory = await managedContext.fetchObjectWithID<Subcategory>(id);
      if (subcategory == null) {
        return AppResponse.ok(message: "Подкатегория не найдена");
      }
      return Response.ok(subcategory);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Подкатегории");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteSubcategory(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final subcategory = await managedContext.fetchObjectWithID<Subcategory>(id);
      if (subcategory == null) {
        return AppResponse.ok(message: "Подкатегория не найдена");
      }
      final qDeleteSubcategory = Query<Subcategory>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteSubcategory.delete();
      return AppResponse.ok(message: "Успешное удаление Подкатегории");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Подкатегории");
    }
  }

}