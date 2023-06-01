import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/subcategory.dart';

import 'my_copany.dart';


class Category extends ManagedObject<_Category> implements _Category {}
class _Category {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? categoryName;
  
  @Serialize(input: true, output: false)
  int? idMycompany;

  ManagedSet<Subcategory>? subcategoryList;
  
  @Relate(#categoryList, isRequired: true, onDelete: DeleteRule.cascade)
  MyCompany? mycompany;
}