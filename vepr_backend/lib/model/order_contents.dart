import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order.dart';
import 'package:vepr_backend/model/selected_product.dart';


class OrderContents extends ManagedObject<_Order_Contents> implements _Order_Contents {}
class _Order_Contents {
  @primaryKey
  int? id;

  @Serialize(input: true, output: false)
  int? idSelectedProduct;

  @Serialize(input: true, output: false)
  int? idOrder;

  @Relate(#orderContentsList, isRequired: true, onDelete: DeleteRule.cascade)
  SelectedProduct? selectedProduct;

  @Relate(#orderContentsList, isRequired: true, onDelete: DeleteRule.cascade)
  Order? order;
}