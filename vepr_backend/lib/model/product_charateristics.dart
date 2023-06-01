import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/characteristics.dart';
import 'package:vepr_backend/model/product.dart';
import 'package:vepr_backend/model/selected_product_characteristics.dart';


class ProductCharacteristics extends ManagedObject<_Product_Characteristics> implements _Product_Characteristics {}
class _Product_Characteristics {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? characteristcValue;

  @Serialize(input: true, output: false)
  int? idProduct;

  @Serialize(input: true, output: false)
  int? idCharacteristics;

  ManagedSet<SelectedProductCharacteristics>? selectedProductCharacteristicsList;

  @Relate(#productCharacteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  Product? product;

  @Relate(#productCharacteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  Characteristics? characteristics;
}