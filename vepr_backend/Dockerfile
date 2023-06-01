# Базовый образ, на основе которого будет построен контейнер
FROM dart:2.18.6-sdk

# Устанавка рабочей директории
WORKDIR /dart_backend

# Копирование исходного кода приложения внутрь контейнера
ADD . /dart_backend/

# Установка необходимых зависимостей
RUN dart pub get
RUN dart pub global activate conduit 4.1.6

EXPOSE 6200

#Запуск миграций и запуск приложения
ENTRYPOINT ["sh", "-c", "dart pub run conduit:conduit db generate && dart pub run conduit:conduit db upgrade && dart pub run conduit:conduit serve --port 6200"]