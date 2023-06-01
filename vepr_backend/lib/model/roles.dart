import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/role_user.dart';



class Roles extends ManagedObject<_Roles> implements _Roles {}
class _Roles {
  @primaryKey
  int? id;
  @Column(indexed: true, useSnakeCaseName: true, nullable: false)
  String? roleName;

  ManagedSet<RoleUser>? roleUserList;
}