import 'dart:io';
import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/my_copany.dart';
import 'package:vepr_backend/model/user_company.dart';
import '../utils/app_response.dart';
import '../utils/app_utils.dart';

class AppCompanyController extends ResourceController {
  AppCompanyController(this.managedContext);

  final ManagedContext managedContext;

  @Operation.post()
  Future<Response> createCompany(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.body() MyCompany myCompany
  ) async {
    try {
      final currentUserId = AppUtils.getIdFromHeader(header);

      if(AppUtils.checkAdmin(header, managedContext) == false)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }

      final qCreateCompanyData = Query<MyCompany>(managedContext)
        ..values.companyName = myCompany.companyName
        ..values.description = myCompany.description
        ..values.urlLogo = myCompany.urlLogo
        ..values.logoName = myCompany.logoName;

      await qCreateCompanyData.insert();

      final qGetCreateCompany = Query<MyCompany>(managedContext)..where((x) => x.companyName).equalTo(qCreateCompanyData.values.companyName);

      MyCompany? createCompany = await qGetCreateCompany.fetchOne();

      final qCreateUserCompany = Query<UserCompany>(managedContext)
        ..values.user?.id = currentUserId
        ..values.myCompany?.id = createCompany?.id;

      await qCreateUserCompany.insert();

      return AppResponse.ok(message: 'Успешное создание компании');
    } catch (error) {
      return AppResponse.serverError(error, message: 'Ошибка создания компании');
    }
  }

  @Operation.put('id')
  Future<Response> updateCompany(
      @Bind.header(HttpHeaders.authorizationHeader) String header,
      @Bind.path("id") int id,
      @Bind.body() MyCompany bodyMyCompany
  ) async {
    try {
      final myCompany = await managedContext.fetchObjectWithID<MyCompany>(id);
      if (myCompany == null) {
        return AppResponse.ok(message: "Данные компании не найдены");
      }
      final qUpdateMyCompany = Query<MyCompany>(managedContext)
        ..where((x) => x.id).equalTo(id)
        ..values.companyName = bodyMyCompany.companyName
        ..values.description = bodyMyCompany.description
        ..values.urlLogo = bodyMyCompany.urlLogo
        ..values.logoName = bodyMyCompany.logoName;

      await qUpdateMyCompany.update();

      return AppResponse.ok(message: 'Данные компании успешно обновлены');

    } catch (e) {
      return AppResponse.serverError(e);
    }
  }

  @Operation.get()
  Future<Response> getMyCompanyFromID() async {
    try {
      /*final currentUserId = AppUtils.getIdFromHeader(header);

      final qGetRoleUser = Query<RoleUser>(managedContext)..where((element) => element.user!.id).equalTo(currentUserId)..where((x) => x.roles!.id).equalTo(1);

      final GetRoleUser = await qGetRoleUser.fetchOne();

      if(GetRoleUser == null)
      {
        return AppResponse.ok(message: "Недостаточно прав, обратитесь к администратору");
      }*/

      final qGetUserCompany= Query<UserCompany>(managedContext)..where((x) => x.id).equalTo(1);

      final UserCompany? company = await qGetUserCompany.fetchOne();

      if(company == null)
      {
        return AppResponse.ok(message: "Данные о компании не заполнены");
      }
      
      final myCompany = await managedContext.fetchObjectWithID<MyCompany>(company.myCompany?.id);
      return Response.ok(myCompany);
    } catch (error) {
      return AppResponse.serverError(error, message: "Ошибка получения Компании");
    }
  }


 
  


  

}