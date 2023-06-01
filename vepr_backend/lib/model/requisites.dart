import 'package:conduit/conduit.dart';

import 'my_copany.dart';


class Requisites extends ManagedObject<_Requisites> implements _Requisites {}
class _Requisites {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? requisitesName;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? requisitesValue;

  @Serialize(input: true, output: false)
  int? idMycompany;
  
  @Relate(#requisitesList, isRequired: true, onDelete: DeleteRule.cascade)
  MyCompany? mycompany;
}