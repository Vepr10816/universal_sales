import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/user.dart';
import 'my_copany.dart';


class UserCompany extends ManagedObject<_UserCompany> implements _UserCompany {}
class _UserCompany {
  @primaryKey
  int? id;

  @Serialize(input: true, output: false)
  int? idUser;

  @Serialize(input: true, output: false)
  int? idMyCompany;

  @Relate(#userCompanyList, isRequired: true, onDelete: DeleteRule.cascade)
  User? user;

  @Relate(#userCompanyList, isRequired: true, onDelete: DeleteRule.cascade)
  MyCompany? myCompany;
}