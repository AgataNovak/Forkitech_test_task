Данное приложение является микросервисом, базирующимся на технологии фреймворка FastAPI, в функционал которого входит обращение к сервису tron и получение запрашиваемых данных о состоянии кошелька по его адресу.

Основной функциональный код располагается в директории app, тесты функционального кода в директории tests.

Стек проекта:
FastAPI, Tronpy, SQLAlchemy, Pytest

Для запуска тестов "pytest run tests"

Для использования приложения на локальном сервере:
Запуск приложения при помощи Run FastApi (требуется конфигурация запуска в зависимости от среды запуска проекта)
Переход в <ВАШ АДРЕС СЕРВЕРА ИЛИ СТАНДАРТНЫЙ ЛОКАЛЬНЫЙ АДРЕС - 127.0.0.1:8000>/docs
Использование эндпоинта post по адресу запроса /wallet с передачей данных в поле "address" в качестве актуального адреса для получения ответа.
