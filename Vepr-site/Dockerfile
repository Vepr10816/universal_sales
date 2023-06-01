FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /vepr-site

# копирование csproj и восстанавление зависимостей
COPY *.csproj ./
RUN dotnet restore

# копирование всего остального и собирка приложения
COPY . ./
RUN dotnet publish -c Release -o out

# сборка контейнера
FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS runtime
WORKDIR /vepr-site
COPY --from=build /vepr-site/out ./
ENTRYPOINT ["dotnet", "Vepr-site.dll"]