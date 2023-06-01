import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order.dart';
import 'package:vepr_backend/model/status.dart';


class OrderStatus extends ManagedObject<_Order_Status> implements _Order_Status {}
class _Order_Status {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  DateTime? dateStatus;

  @Serialize(input: true, output: false)
  int? idOrder;

  @Serialize(input: true, output: false)
  int? idStatus;

  @Relate(#orderStatusList, isRequired: true, onDelete: DeleteRule.cascade)
  Order? order;

  @Relate(#orderStatusList, isRequired: true, onDelete: DeleteRule.cascade)
  Status? status;
}