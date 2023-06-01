import 'dart:io';

import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order_status.dart';
import '../model/order.dart';
import '../model/order_contents.dart';
import '../model/product.dart';
import '../model/response.dart';
import '../model/selected_product.dart';
import '../model/selected_product_characteristics.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppAllOrderController extends ResourceController {
  AppAllOrderController(this.managedContext);

  final ManagedContext managedContext;


  @Operation.get("idStatus")
  Future<Response> getFullOrder(
  @Bind.header(HttpHeaders.authorizationHeader) String header,
  @Bind.path("idStatus") int idStatus)
  async {
    try {
      
      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final qGetOrder = Query<Order>(managedContext)
      ..sortBy((x) => x.orderDate, QuerySortOrder.ascending)
      ..join(set: (x) => x.orderContentsList)
      ..join(set: (x) => x.orderStatusList)
      ..join(object: (x) => x.user);

      List<Order> orderList = await qGetOrder.fetch();

      if (orderList.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Список пуст"));
      }

      List<Order> orderListConteiner = <Order>[];
      for(Order order in orderList)
      {
        orderListConteiner.add(order);
      }

      for(Order order in orderListConteiner)
      {
        final ManagedSet<OrderStatus>? statusList = order.orderStatusList;
        int counterIdStatus = 0;
        for(OrderStatus status in statusList!)
        {
          if(idStatus == 2 && status.status!.id == idStatus)
          {
            counterIdStatus += 1;
          }
          if(idStatus == 1 && status.status!.id == 2)
          {
            counterIdStatus = 0;
            break;
          }
          if(idStatus == 1 && status.status!.id == idStatus){
            counterIdStatus += 1;
          }
          
        }
        if(counterIdStatus == 0)
        {
          orderList.remove(order);
        }
      }

      List<Map> finalMap = <Map>[];

      for(Order order in orderList)
      {
        ManagedSet<OrderContents>? orderContentsList = order.orderContentsList;
        //List<int> idSelectedProductList = <int>[];
        List<Map> productsMap = <Map>[];
        for(OrderContents orderContents in orderContentsList!)
        {
          final selectedProduct = await managedContext.fetchObjectWithID<SelectedProduct>(orderContents.selectedProduct?.id);
          int? idSelectedProduct = selectedProduct?.id;
          //idSelectedProductList.add(idSelectedProduct!);
          int? selectedProductQuantity = selectedProduct?.productQuantity;
          final product = await managedContext.fetchObjectWithID<Product>(selectedProduct?.product?.id);
           //Map productMap = product!.asMap();
          final qGetselectedProductCharacteristicsList = Query<SelectedProductCharacteristics>(managedContext)
                                                      ..where((x) => x.selectedProduct!.id).equalTo(idSelectedProduct)
                                                        ..join(object: (x) => x.productCharacteristics);
          List<SelectedProductCharacteristics> selectedProductCharacteristicsList = 
                                                        await qGetselectedProductCharacteristicsList.fetch();

          List<Map> mapSelectedProductCharacteristicsList = <Map>[];
          for(SelectedProductCharacteristics item in selectedProductCharacteristicsList)
          {
            mapSelectedProductCharacteristicsList.add(item.asMap());
          }
           
          productsMap.add
          (
            {
              "idSelectedProduct": idSelectedProduct, 
              "Quantity": selectedProductQuantity,
              "Product": product!.asMap(),
              "SelectedProductCharacteristics": mapSelectedProductCharacteristicsList
            }
          );                        
            
        }
        var map = 
        {
          "Order":order.asMap(),
          "Products": productsMap
        };
        finalMap.add(map);
      }

      if (finalMap.isEmpty)
      {
        return Response.notFound(body: ModelResponse(data: [], message: "Список пуст"));
      }

      return Response.ok(finalMap);
    } catch (e) {
      return AppResponse.serverError(e);
    }
  }
}