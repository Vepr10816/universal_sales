import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/category.dart';
import 'package:vepr_backend/model/product.dart';

import 'characteristics.dart';
import 'my_copany.dart';


class Subcategory extends ManagedObject<_Subcategory> implements _Subcategory {}
class _Subcategory {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? subcategoryName;
  
  @Serialize(input: true, output: false)
  int? idCategory;

  ManagedSet<Characteristics>? characteristicsList;

  ManagedSet<Product>? productList;
  
  @Relate(#subcategoryList, isRequired: true, onDelete: DeleteRule.cascade)
  Category? category;
}