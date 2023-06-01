import 'dart:io';
import 'package:conduit/conduit.dart';
import 'package:vepr_backend/vepr_backend.dart';


///Запуск программы.
///[arguments] - стандартные аргументы Dart запуска.
void main(List<String> arguments) async{
  //Порт на котором запускается программа.
  final port = int.parse(Platform.environment["PORT"] ?? '6200');

  //Регистрация прописанного сервиса.
  final service = Application<AppService>()..options.port = port;

  //Запуск с транслированием состояния API.
  await service.start(numberOfInstances: 3, consoleLogging: true);
}

