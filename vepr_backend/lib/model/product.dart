import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/currency.dart';
import 'package:vepr_backend/model/product_charateristics.dart';
import 'package:vepr_backend/model/product_photos.dart';
import 'package:vepr_backend/model/selected_product.dart';
import 'package:vepr_backend/model/subcategory.dart';

class Product extends ManagedObject<_Product> implements _Product {}

class _Product{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? productName;
  @Column(indexed: true, nullable: true, useSnakeCaseName: true)
  String? description;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  double? productPrice;

  @Serialize(input: true, output: false)
  int? idCurrency;

  @Serialize(input: true, output: false)
  int? idSubcategory;

  ManagedSet<ProductCharacteristics>? productCharacteristicsList;

  ManagedSet<ProductPhotos>? productPhotosList;

  ManagedSet<SelectedProduct>? selectedProductList;

  @Relate(#productList, isRequired: true, onDelete: DeleteRule.cascade)
  Currency? currency;

  @Relate(#productList, isRequired: true, onDelete: DeleteRule.cascade)
  Subcategory? subcategory;

}