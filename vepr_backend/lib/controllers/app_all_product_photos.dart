import 'dart:io';

import 'package:conduit/conduit.dart';
import '../model/product_photos.dart';
import '../model/response.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppAllProductPhotosController extends ResourceController {
  AppAllProductPhotosController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idProduct")
  Future<Response> getFullProductPhotos(@Bind.path("idProduct") int idProduct,
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetProductPhotos = Query<ProductPhotos>(managedContext)..where((x) => x.product?.id).equalTo(idProduct);

      final List<ProductPhotos> list = await qGetProductPhotos.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], 
                                message: "У данного товара нет фотографий"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.delete("idProduct")
  Future<Response> deleteProduct(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("idProduct") int idProduct,
  ) async {
    try {
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      final qGetProductPhotos = Query<ProductPhotos>(managedContext)..where((x) => x.product?.id).equalTo(idProduct);
      final List<ProductPhotos> listPhotos = await qGetProductPhotos.fetch();
      if (listPhotos == null) {
        return AppResponse.ok(message: "Фотографии не найдены");
      }
      final qDeletePhotos = Query<ProductPhotos>(managedContext)
        ..where((x) => x.product?.id).equalTo(idProduct);
      await qDeletePhotos.delete();
      return AppResponse.ok(message: "Успешное удаление  фотографий товара");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка удаления фотографий товара");
    }
  }
}