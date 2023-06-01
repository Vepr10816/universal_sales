Министерство науки и высшего образования Российской Федерации

федеральное государственное бюджетное образовательное учреждение 

высшего образования

«Российский экономический университет имени Г.В. Плеханова»

Московский приборостроительный техникум
(Дипломная работа)


|На тему:|Разработка <a name="_hlk136221756"></a>кроссплатформенного программного комплекса универсальных продаж (на примере ООО «ЛаБС»)|
| :-: | - |

ВЕПРИЦКОГО АРТЁМА НИКОЛАЕВИЧА

Студент 4 курса группы П50-2-19

по специальности 09.02.07 «Информационные системы и программирование» 

для присвоения квалификации: программист

Форма обучения: очная

Руководитель:		 / Шимбирёв Андрей Андреевич /

Консультант:		 / Завьялова Анастасия Дмитриевна /

Студент:		 / Веприцкий Артём Николаевич /



Допущен к защите

Приказ от «18» мая 2023 г. № 18.01-354


2023

<a name="_hlk136221756"></a>Описание|
| - |
Целью разработки является создание полноценного программного коплекса основывающимся на продаже всего, что пожелает продавец: начиная от товаров и заканчивая услугами. *Universal* - универсальность, система торговли подстраивается под желания заказчика.

 <a name="_hlk136221756"></a>Инструкция запуска|
| - |

В файле /Vepr-bot/.env в параметре "BOT_TOKEN" указать токен своего telegram-бота.

В файле /Vepr-site/Vepr-site/appsettings.json в параметре "ApiToken" указать токен своего telegram-бота, в параметре "BotUserName" указать имя своего telegram-бота.

В файле /Vepr-bot/config/role.py в списке "admins" указать свой уникальный индетификатор пользователя Telegram.

Для авторизации пользователей на сайте необходимо задать домен сайта telegram-боту через BotFather.

Требования к ПО: наличие доступа в интернет, наличие Docker Desktop.

Полная инструкция находится в файле РУКОВОДСТВО ПОЛЬЗОВАТЕЛЯ.

<a name="_hlk136221756"></a>Отдельное спасибо|
| - |
 Шимбирёву Андрею Андреевичу, Пахомову Даниилу Александровичу, Горбунову Антону Дмитриевичу, Михайлину Никите Александровичу, Лясникову Антону Олеговичу, Волкову Роману Юрьевичу, Волковой Галине Юрьевне, Соколовой Ларисе Алексеевне, Гордюшину Дмитрию Александровичу, Аксенову Андрею Алексеевичу, Игнатову Никите Сергеевичу, Веселову Михаилу Владимировичу.

 ![](Логотип.png)