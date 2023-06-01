import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/product_charateristics.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppProductCharacteristicsController extends ResourceController {
  AppProductCharacteristicsController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createProductCharacteristics(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() ProductCharacteristics bodyProductCharacteristics
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateProductCharacteristicsData = Query<ProductCharacteristics>(managedContext)
        ..values.characteristcValue = bodyProductCharacteristics.characteristcValue
        ..values.product!.id = bodyProductCharacteristics.idProduct
        ..values.characteristics!.id = bodyProductCharacteristics.idCharacteristics;

      await qCreateProductCharacteristicsData.insert();

      return AppResponse.ok(message: 'Успешное создание Характеристик');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Характеристик');
    }
  }

  @Operation.put('id')
  Future<Response> updateProductCharacteristics(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() ProductCharacteristics bodyProductCharacteristics
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final characteristc = await managedContext.fetchObjectWithID<ProductCharacteristics>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Характеристики не найдены");
      }
      final qUpdateProductCharacteristics = Query<ProductCharacteristics>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.characteristcValue = bodyProductCharacteristics.characteristcValue
        ..values.product!.id = bodyProductCharacteristics.idProduct
        ..values.characteristics!.id = bodyProductCharacteristics.idCharacteristics;
      await qUpdateProductCharacteristics.update();

      return AppResponse.ok(message: 'Характеристики обновлены');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getProductCharacteristicsFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final characteristc = await managedContext.fetchObjectWithID<ProductCharacteristics>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Характеристики не найдены");
      }
      return Response.ok(characteristc);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Характеристик");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteProductCharacteristics(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final characteristc = await managedContext.fetchObjectWithID<ProductCharacteristics>(id);
      if (characteristc == null) {
        return AppResponse.ok(message: "Характеристики не найдены");
      }
      final qDeleteProductCharacteristics = Query<ProductCharacteristics>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteProductCharacteristics.delete();
      return AppResponse.ok(message: "Успешное удаление Характеристик");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Характеристик");
    }
  }

}