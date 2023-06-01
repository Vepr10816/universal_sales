import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/product.dart';

class Currency extends ManagedObject<_Currency> implements _Currency {}

class _Currency{
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? currencyName;

  ManagedSet<Product>? productList;
}