import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/product_charateristics.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppAllProductCharacteristicsController extends ResourceController {
  AppAllProductCharacteristicsController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idProduct")
  Future<Response> getFullProductCharacteristics(@Bind.path("idProduct") int idProduct,
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetProductCharacteristics = Query<ProductCharacteristics>(managedContext)..where((x) => x.characteristics?.id).equalTo(idProduct);

      final List<ProductCharacteristics> list = await qGetProductCharacteristics.fetch();

      if (list.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], 
                                message: "У данного товара нет характеристик"));
      }

      return Response.ok(list);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}