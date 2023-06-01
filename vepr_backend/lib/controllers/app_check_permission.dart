import 'package:conduit/conduit.dart';

import '../model/role_user.dart';
import '../utils/app_utils.dart';

class CheckPermission {
  Future<bool> checkAdmin(String header, managedContext) async{
      final currentUserId = AppUtils.getIdFromHeader(header);

      final qGetRoleUser = Query<RoleUser>(managedContext)..where((element) => element.user!.id).equalTo(currentUserId)..where((x) => x.roles!.id).equalTo(1);

      final getRoleUser = await qGetRoleUser.fetchOne();

      if(getRoleUser == null) {
        return false;
      } else {
        return true;
      }
  }
}