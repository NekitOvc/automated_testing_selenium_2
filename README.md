# automated_testing_selenium_2

Объект тестирования: web-приложение "Simple Calculator" https://testpages.herokuapp.com/styled/calculator

Требования:
1. Разработать тест-кейсы;
2. Провести автоматизированное тестирование продукта;
3. Оформить описание обнаруженных багов

test_checking_mathematical_operations.py - автотесты основных математических операций

test_checking_decimals_1.py - автотесты математических операций, где **запятая** является разделителем между целой и дробной частью числа

test_checking_decimals_2.py - автотесты математических операций, где **точка** является разделителем между целой и дробной частью числа

test_other_operations.py - автотесты математических операций, не поддающихся вычислению

Для запуска тестов требуется предварительная установка библиотек **pytest** **selenium**, **requests**, а также скачивание драйвера, совместимого с браузером. Скачать можно по ссылке: https://chromedriver.chromium.org/downloads

https://docs.google.com/spreadsheets/d/1h-Ou53Tw48hb9rPU327BVUvc1U0-YIEk0fWsGDCVZzc/edit#gid=854680875 - ссылка на тест-кейсы
