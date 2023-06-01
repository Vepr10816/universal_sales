import 'dart:io';
import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/characteristics.dart';
import 'package:vepr_backend/model/product_charateristics.dart';
import '../model/response.dart';
import '../utils/app_response.dart';

class AppSelectableCharacteristicsController extends ResourceController {
  AppSelectableCharacteristicsController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get()
  Future<Response> getFullAddresses(@Bind.query('idSubcategory') int idSubcategory,
  @Bind.query('idProduct') int idProduct,
  @Bind.header(HttpHeaders.authorizationHeader) String header) 
  async {
    try {

      final qGetSelectableCharacteristics = Query<Characteristics>(managedContext)..where((x) => x.subcategory?.id).equalTo(idSubcategory);

      final List<Characteristics> listCharacteristics = await qGetSelectableCharacteristics.fetch();

      if (listCharacteristics.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одной характеристики"));
      }

      final List<ProductCharacteristics> listProductCharacteristics = <ProductCharacteristics>[];
      for(Characteristics item in listCharacteristics)
      {
        if(item.selectable == true)
        {
          final qGetProductCharacteristics = Query<ProductCharacteristics>(managedContext)
          ..where((x) => x.characteristics?.id).equalTo(item.id)
          ..where((x) => x.product?.id).equalTo(idProduct)
          ..join(object: (x) => x.characteristics)
          ..join(object: (x) => x.product);
          final List<ProductCharacteristics> productCharacteristics = await qGetProductCharacteristics.fetch();
          for(ProductCharacteristics product in productCharacteristics)
          {
            listProductCharacteristics.add(product);
          }
        }

      }

      if (listProductCharacteristics.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Нет ни одной выбираемой характеристики"));
      }

      return Response.ok(listProductCharacteristics);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}