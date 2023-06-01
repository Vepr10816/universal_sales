import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/characteristics.dart';

class DataType extends ManagedObject<_DataType> implements _DataType {}

class _DataType{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? typeName;

  ManagedSet<Characteristics>? characteristicsList;
}