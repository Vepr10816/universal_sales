import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/product.dart';

class ProductPhotos extends ManagedObject<_Product_Photos> implements _Product_Photos {}

class _Product_Photos{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: true)
  String? urlPhoto;
  @Column(indexed: true, useSnakeCaseName: true, nullable: true)
  String? photoName;

  @Serialize(input: true, output: false)
  int? idProduct;
  
  @Relate(#productPhotosList, isRequired: true, onDelete: DeleteRule.cascade)
  Product? product;

}