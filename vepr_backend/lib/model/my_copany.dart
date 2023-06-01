import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/addresses.dart';
import 'package:vepr_backend/model/requisites.dart';
import 'package:vepr_backend/model/user_company.dart';
import 'package:vepr_backend/model/category.dart';

class MyCompany extends ManagedObject<_MyCompany> implements _MyCompany {}

class _MyCompany{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? companyName;
  @Column(indexed: true, useSnakeCaseName: true)
  String? description;
  @Column(indexed: true, nullable: true, useSnakeCaseName: true)
  String? urlLogo;
  @Column(indexed: true, nullable: true, useSnakeCaseName: true)
  String? logoName;

  ManagedSet<Requisites>? requisitesList;
  
  ManagedSet<Addresses>? addressesList;

  ManagedSet<Category>? categoryList;

  ManagedSet<UserCompany>? userCompanyList;

}