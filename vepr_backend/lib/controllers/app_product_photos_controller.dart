import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/product_photos.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppProductPhotosController extends ResourceController {
  AppProductPhotosController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createProduct(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() ProductPhotos bodyProduct
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateProductData = Query<ProductPhotos>(managedContext)
        ..values.urlPhoto = bodyProduct.urlPhoto
        ..values.photoName = bodyProduct.photoName
        ..values.product!.id = bodyProduct.idProduct;

      await qCreateProductData.insert();

      return AppResponse.ok(message: 'Успешное создание Фотографии товара');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Фотографии товара');
    }
  }

  @Operation.put('id')
  Future<Response> updateProduct(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() ProductPhotos bodyProduct
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final productPhoto = await managedContext.fetchObjectWithID<ProductPhotos>(id);
      if (productPhoto == null) {
        return AppResponse.ok(message: "Фотография товара не найдена");
      }
      final qUpdateProduct = Query<ProductPhotos>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.urlPhoto = bodyProduct.urlPhoto
       ..values.photoName = bodyProduct.photoName
        ..values.product!.id = bodyProduct.idProduct;
      await qUpdateProduct.update();

      return AppResponse.ok(message: 'Фотография товара обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getProductFromID(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final productPhoto = await managedContext.fetchObjectWithID<ProductPhotos>(id);
      if (productPhoto == null) {
        return AppResponse.ok(message: "Фотография товара не найдена");
      }
      return Response.ok(productPhoto);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Фотографии товара");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteProduct(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final productPhoto = await managedContext.fetchObjectWithID<ProductPhotos>(id);
      if (productPhoto == null) {
        return AppResponse.ok(message: "Фотография товара не найдена");
      }
      final qDeleteProduct = Query<ProductPhotos>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteProduct.delete();
      return AppResponse.ok(message: "Успешное удаление Фотографии товара");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Фотографии товара");
    }
  }

}