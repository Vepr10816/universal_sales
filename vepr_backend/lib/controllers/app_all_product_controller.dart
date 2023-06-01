import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/product.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllProductController extends ResourceController {
  AppAllProductController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idSubcategory")
  Future<Response> getFullProduct(@Bind.path("idSubcategory") int idSubcategory) 
  async {
    try {

      final qGetProduct = Query<Product>(managedContext)..where((x) => x.subcategory?.id).equalTo(idSubcategory)
      ..join(set: (x) => x.productPhotosList)
      ..join(set: (x) => x.productCharacteristicsList)
      ..join(object: (x) => x.currency)
      ..join(object: (x) => x.subcategory);

      final List<Product> list = await qGetProduct.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одного товара"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}