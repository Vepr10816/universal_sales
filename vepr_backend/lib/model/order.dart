import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order_contents.dart';
import 'package:vepr_backend/model/order_status.dart';
import 'package:vepr_backend/model/user.dart';


class Order extends ManagedObject<_Order> implements _Order {}
class _Order {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: true)
  String? comment;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  double? totalPrice;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false, defaultValue: "now()")
  DateTime? orderDate;

  @Serialize(input: true, output: false)
  int? idUser;
  
  ManagedSet<OrderStatus>? orderStatusList;

  ManagedSet<OrderContents>? orderContentsList;

  @Relate(#orderList, isRequired: true, onDelete: DeleteRule.cascade)
  User? user;
}