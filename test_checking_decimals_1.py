"""Математические операции, где запятая является разделителем между целой и дробной частью числа"""

from test_options import testing, get_chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

import time


# TEST_06
# проверка любой математической операции десятичных дробей
# запятая является разделителем между целой и дробной частью числа (2,5 + 5,2)
def test_operation_1(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys('2,5')
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys('5,2')
    time.sleep(1)
    # нажать на выбор операции
    selenium.find_element(By.ID, 'function').click()
    time.sleep(1)
    # выбрать любую операцию
    selenium.find_element(By.XPATH, f'//*[@id="function"]/option[{randint(1, 4)}]').click()
    time.sleep(2)
    # нажать Calculate
    selenium.find_element(By.XPATH, '//*[@id="calculate"]').click()
    time.sleep(2)

    selenium.save_screenshot('test_operation_1.png')

    assert selenium.find_element(By.ID, 'answer').text == 'ERR', print('Тест провален')