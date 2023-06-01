import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/data_type.dart';
import 'package:vepr_backend/model/pre_values.dart';
import 'package:vepr_backend/model/product_charateristics.dart';
import 'package:vepr_backend/model/subcategory.dart';


class Characteristics extends ManagedObject<_Characteristics> implements _Characteristics {}
class _Characteristics {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? characteristicName;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false, defaultValue: "false")
  bool? selectable;
  
  @Serialize(input: true, output: false)
  int? idDatatype;

  @Serialize(input: true, output: false)
  int? idSubcategory;

  ManagedSet<PreValues>? preValuesList;

  ManagedSet<ProductCharacteristics>? productCharacteristicsList;
  
  @Relate(#characteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  DataType? datatype;

  @Relate(#characteristicsList, isRequired: true, onDelete: DeleteRule.cascade)
  Subcategory? subcategory;
}