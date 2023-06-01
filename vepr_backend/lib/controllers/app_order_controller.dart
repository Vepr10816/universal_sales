import 'dart:io';
import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order_contents.dart';
import 'package:vepr_backend/model/order_status.dart';
import 'package:vepr_backend/model/product.dart';
import '../model/order.dart';
import '../model/selected_product.dart';
import '../model/selected_product_characteristics.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppOrderController extends ResourceController {
  AppOrderController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createOrder(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.query('idProductList') List<int> idProductList,
      @Bind.query('quantityList') List<int> quantityList,
      @Bind.query('totalPrice') double totalPrice,
      @Bind.query('comment') String comment,
      @Bind.query('idProductCharacteristicsList') List<int> idProductCharacteristicsList,
  ) async {
    try {
      List<int> idSelectedProductList = <int>[];
      List<int> idProductCharacteristicsListFixedLength = idProductCharacteristicsList;
      List<int> idProductCharacteristicsListForFixedLength = <int>[];
      for(int i = 0; i<idProductList.length; i++)
      {
        final qCreateSelectedProduct = Query<SelectedProduct>(managedContext)
          ..values.product!.id = idProductList[i]
          ..values.productQuantity = quantityList[i];
        final createdSelectedProduct = await qCreateSelectedProduct.insert();
        int? idSelectedProduct = createdSelectedProduct.id;

        for(int j = 0; j<idProductCharacteristicsListFixedLength.length; j++)
        {
          if(idProductCharacteristicsListFixedLength[j] == 0)
          {
            idProductCharacteristicsListForFixedLength.add(idProductCharacteristicsListFixedLength[j]);
            break;
          }
          else{
            final qCreateSelectedProductCharacteristics = Query<SelectedProductCharacteristics>(managedContext)
            ..values.selectedProduct!.id = idSelectedProduct
            ..values.productCharacteristics!.id = idProductCharacteristicsListFixedLength[j];
            await qCreateSelectedProductCharacteristics.insert();
            idProductCharacteristicsListForFixedLength.add(idProductCharacteristicsListFixedLength[j]);
          }
        }
        for(int item in idProductCharacteristicsListForFixedLength)
        {
          idProductCharacteristicsList.remove(item);
          idProductCharacteristicsListFixedLength.remove(item);
        }
        idProductCharacteristicsListForFixedLength.clear();
        idSelectedProductList.add(idSelectedProduct!);
      }

      final qCreateOrder = Query<Order>(managedContext)
      ..values.comment = comment
      ..values.totalPrice = totalPrice
      ..values.user!.id = AppUtils.getIdFromHeader(header);

      final createdOrder = await qCreateOrder.insert();
      
      final qCreateOrderStatus = Query<OrderStatus>(managedContext)
      ..values.dateStatus = DateTime.now()
      ..values.order!.id = createdOrder.id
      ..values.status!.id = 1;

      await qCreateOrderStatus.insert();

      for(int i = 0; i < idSelectedProductList.length; i++)
      {
        final qCreateOrderContent = Query<OrderContents>(managedContext)
        ..values.order!.id = createdOrder.id
        ..values.selectedProduct!.id = idSelectedProductList[i];
        await qCreateOrderContent.insert();
      }

      return AppResponse.ok(message: "Успешное оформление заказа");
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания Заказ');
    }
  }

  @Operation.put('id')
  Future<Response> updateOrder(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() Order bodyOrder
  ) async {
    try {

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }
      
      final order = await managedContext.fetchObjectWithID<Order>(id);
      if (order == null) {
        return AppResponse.ok(message: "Заказ не найден");
      }
      

      return AppResponse.ok(message: 'Заказ обновлен');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get()
  Future<Response> getOrderFromUser(
    @Bind.header(HttpHeaders.authorizationHeader) String header
  ) async {
    try {
      final idUser = AppUtils.getIdFromHeader(header);
      final qGetOrder = Query<Order>(managedContext)
      ..where((x) => x.user?.id).equalTo(idUser)
      ..sortBy((x) => x.orderDate, QuerySortOrder.ascending)
      ..join(set: (x) => x.orderContentsList)
      ..join(set: (x) => x.orderStatusList);

      final List<Order> orderList = await qGetOrder.fetch();

      if (orderList.isEmpty) {
        return AppResponse.ok(message: "У вас нет ни одного заказа");
      }

      List<Map> finalMap = <Map>[];

      for(Order order in orderList)
      {
        ManagedSet<OrderContents>? orderContentsList = order.orderContentsList;
        List<Map> productsMap = <Map>[];
        for(OrderContents orderContents in orderContentsList!)
        {
          final selectedProduct = await managedContext.fetchObjectWithID<SelectedProduct>(orderContents.selectedProduct?.id);
          int? idSelectedProduct = selectedProduct?.id;
          int? selectedProductQuantity = selectedProduct?.productQuantity;
          final product = await managedContext.fetchObjectWithID<Product>(selectedProduct?.product?.id);
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



      /*Product product = Product();
      Product product2 = Product();
      product.description = "erev";
      product.productName = "jencihren";
      product2.description = "qwer";
      product2.productName = "zcvbn";
      List<Map> productList = [product.asMap(), product2.asMap()];

      Order order = Order();
      order.comment = "jdjiv";
      order.id = 10;
      order.totalPrice = 1700;
      Order order2 = Order();
      order2.comment = "jdjiv";
      order2.id = 10;
      order2.totalPrice = 1700;
      
      OrderStatus orderStatus = OrderStatus();
      orderStatus.dateStatus = DateTime.now();
      //orderStatus.status!.statusName = "Лох";
      OrderStatus orderStatus2 = OrderStatus();
      orderStatus2.dateStatus = DateTime.now();
      //orderStatus2.status!.statusName = "НеЛох";
      List<Map> orderStatusList = [orderStatus.asMap(), orderStatus2.asMap()];
      

      var map = 
      {
        "order": order.asMap(),
        "status": orderStatusList,
        "products": [{"Product":productList, "Characteristics": 22}],
      };
      var map1 = {"Order":{"id":1, "name": "nameOrder"}, "Book":{"id":1, "name": "nameBook"}};
      final map2 = <String, Map<String, Object>>{"Order2":{"id":1, "name": "nameOrder2"}, "Book2":{"id":1, "name": "nameBook2"}};
      map1.addEntries(map2.entries);
      List<Map> listMap= [map, map1];*/
      return Response.ok(finalMap);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Заказов");
    }
  }


  @Operation.delete("id")
  Future<Response> deleteOrder(
    @Bind.header(HttpHeaders.authorizationHeader) String header,
    @Bind.path("id") int id,
  ) async {
    try {
      final qGetOrder = Query<Order>(managedContext)..where((x) => x.id).equalTo(id);
      final order = await qGetOrder.fetchOne();

      if (order == null) 
      {
        return AppResponse.ok(message: "Заказ не найден");
      }

      final qGetOrderContents = Query<OrderContents>(managedContext)..where((x) => x.order!.id).equalTo(order.id);
      List<OrderContents> orderContentsList = await qGetOrderContents.fetch();

      for(OrderContents orderContents in orderContentsList)
      {
        final qDeleteSelectedProduct = Query<SelectedProduct>(managedContext)
        ..where((x) => x.id).equalTo(orderContents.selectedProduct!.id);
        await qDeleteSelectedProduct.delete();
      }
  
      final qDeleteOrder = Query<Order>(managedContext)
        ..where((x) => x.id).equalTo(id);
      await qDeleteOrder.delete();
      return AppResponse.ok(message: "Успешная отмена Заказа");
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка отмены Заказа");
    }
  }

}