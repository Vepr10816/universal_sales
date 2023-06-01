import 'package:conduit/conduit.dart';
import 'characteristics.dart';

class PreValues extends ManagedObject<_PreValues> implements _PreValues {}

class _PreValues{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? preValue;

  @Serialize(input: true, output: false)
  int? idCharacteristics;
  
  @Relate(#preValuesList, isRequired: true, onDelete: DeleteRule.cascade)
  Characteristics? characteristics;

}