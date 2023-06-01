import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/roles.dart';
import 'package:vepr_backend/model/user.dart';




class RoleUser extends ManagedObject<_RoleUser> implements _RoleUser {}
class _RoleUser {
  @primaryKey
  int? id;

  @Serialize(input: true, output: false)
  int? roles_id;

  @Serialize(input: true, output: false)
  int? user_id;

  @Relate(#roleUserList, isRequired: true, onDelete: DeleteRule.cascade)
  Roles? roles;

  @Relate(#roleUserList, isRequired: true, onDelete: DeleteRule.cascade)
  User? user;
}