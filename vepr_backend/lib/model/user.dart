import 'package:conduit/conduit.dart';
import 'package:vepr_backend/model/order.dart';
import 'package:vepr_backend/model/role_user.dart';
import 'package:vepr_backend/model/user_company.dart';




class User extends ManagedObject<_User> implements _User {}

class _User {
  @primaryKey
  int? id;
  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? email;
  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? lastName;
  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? firstName;
  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? middleName;
  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? userName;
  @Serialize(input: true, output: false)
  String? password;
  @Column(nullable: true, useSnakeCaseName: true)
  String? accessToken;
  @Column(nullable: true, useSnakeCaseName: true)
  String? refreshToken;

  @Column(omitByDefault: true, nullable: true, useSnakeCaseName: true)
  String? salt;
  @Column(omitByDefault: true, nullable: true, useSnakeCaseName: true)
  String? hashPassword;

  @Column(unique: true, indexed: true, nullable: true, useSnakeCaseName: true)
  String? tgId;

  ManagedSet<RoleUser>? roleUserList;

  ManagedSet<UserCompany>? userCompanyList;

  ManagedSet<Order>? orderList;
}