import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/product.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppProductController extends ResourceController {
  AppProductController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createProduct(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() Product bodyProduct
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateProductData = Query<Product>(managedContext)
        ..values.productName = bodyProduct.productName
        ..values.description = bodyProduct.description
        ..values.productPrice = bodyProduct.productPrice
        ..values.currency!.id = bodyProduct.idCurrency
        ..values.subcategory!.id = bodyProduct.idSubcategory;

      await qCreateProductData.insert();

      final qGetProduct = Query<Product>(managedContext)
      ..where((x) => x.subcategory?.id).equalTo(bodyProduct.idSubcategory)
      ..sortBy((x) => x.id, QuerySortOrder.ascending);
      final List<Product> list = await qGetProduct.fetch();
      final product = list.last;
      String idProduct = product.id.toString();

      return AppResponse.ok(message: idProduct);
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Товара');
    }
  }

  @Operation.put('id')
  Future<Response> updateProduct(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Product bodyProduct
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final product = await managedContext.fetchObjectWithID<Product>(id);
      if (product == null) {
        return AppResponse.ok(message: "Товар не найдена");
      }
      final qUpdateProduct = Query<Product>(managedContext)
        ..where((x) => x.id).equalTo(id)
       ..values.productName = bodyProduct.productName
        ..values.description = bodyProduct.description
        ..values.productPrice = bodyProduct.productPrice
        ..values.currency!.id = bodyProduct.idCurrency
        ..values.subcategory!.id = bodyProduct.idSubcategory;
      await qUpdateProduct.update();

      return AppResponse.ok(message: 'Товар обновлена');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get("id")
  Future<Response> getProductFromID(
    @Bind.path("id") int id,
  ) async {
    try {

      final qGetProduct = Query<Product>(managedContext)..where((x) => x.id).equalTo(id)
      ..join(set: (x) => x.productPhotosList)
      ..join(set: (x) => x.productCharacteristicsList)
      ..join(object: (x) => x.currency);

      final List<Product> list = await qGetProduct.fetch();

      final product = await managedContext.fetchObjectWithID<Product>(id);
      
      if (product == null) {
        return AppResponse.ok(message: "Товар не найдена");
      }

      product.productPhotosList = list[0].productPhotosList;
      product.productCharacteristicsList = list[0].productCharacteristicsList;
      product.currency = list[0].currency;

      return Response.ok(product);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Товара");
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
      final product = await managedContext.fetchObjectWithID<Product>(id);
      if (product == null) {
        return AppResponse.ok(message: "Товар не найдена");
      }
      final qDeleteProduct = Query<Product>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteProduct.delete();
      return AppResponse.ok(message: "Успешное удаление Товара");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления Товара");
    }
  }

}