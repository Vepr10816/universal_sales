import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order_status.dart';


class Status extends ManagedObject<_Status> implements _Status {}
class _Status {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? statusName;
  
  ManagedSet<OrderStatus>? orderStatusList;
}