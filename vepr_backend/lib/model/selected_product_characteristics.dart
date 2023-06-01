import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/product_charateristics.dart';
import 'package:vepr_backend/model/selected_product.dart';


class SelectedProductCharacteristics extends ManagedObject<_Selected_Product_Characteristics> implements _Selected_Product_Characteristics {}
class _Selected_Product_Characteristics {
  @primaryKey
  int? id;

  @Serialize(input: true, output: false)
  int? idSelectedProduct;

  @Serialize(input: true, output: false)
  int? idProductCharacteristics;

  @Relate(#selectedProductCharacteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  SelectedProduct? selectedProduct;

  @Relate(#selectedProductCharacteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  ProductCharacteristics? productCharacteristics;
}