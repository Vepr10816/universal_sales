import 'package:conduit/conduit.dart';

import 'my_copany.dart';


class Addresses extends ManagedObject<_Addresses> implements _Addresses {}
class _Addresses {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? addressName;
  
  @Serialize(input: true, output: false)
  int? idMycompany;
  
  @Relate(#addressesList, isRequired: true, onDelete: DeleteRule.cascade)
  MyCompany? mycompany;
}