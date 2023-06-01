import 'dart:io';
import 'package:conduit/conduit.dart';
import '../model/order_status.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppOrderStatusController extends ResourceController {
  AppOrderStatusController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post("idOrder")
  Future<Response> createOrderStatus(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
       @Bind.path("idOrder") int idOrder,
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateOrderStatusData = Query<OrderStatus>(managedContext)
        ..values.dateStatus = DateTime.now()
        ..values.order!.id = idOrder
        ..values.status!.id = 2;

      await qCreateOrderStatusData.insert();

      return AppResponse.ok(message: 'Успешное Оформление заказа');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка оформления заказа');
    }
  }

}