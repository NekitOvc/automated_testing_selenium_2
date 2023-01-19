"""Математические операции, не поддающиеся вычислению"""

from test_options import testing, get_chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

import time


# TEST_11
# проверка любой математической операции, с применением кириллицы вместо цифр
def test_operation_2(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys('два')
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys('два')
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

    selenium.save_screenshot('test_operation_2.png')

    assert selenium.find_element(By.ID, 'answer').text == 'ERR', print('Тест провален')


# TEST_12
# проверка деления на 0 при введенных данных в первое поле в диапазоне от 1 до 100
def test_operation_3(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys(randint(1, 100))
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys('0')
    time.sleep(1)
    # нажать на выбор операции
    selenium.find_element(By.ID, 'function').click()
    time.sleep(1)
    # выбрать операцию деления
    selenium.find_element(By.XPATH, '//*[@id="function"]/option[4]').click()
    time.sleep(2)
    # нажать Calculate
    selenium.find_element(By.XPATH, '//*[@id="calculate"]').click()
    time.sleep(2)

    selenium.save_screenshot('test_operation_3.png')

    assert selenium.find_element(By.ID, 'answer').text == 'ERR', print('Тест провален')


# TEST_13
# проверка невыполнения операций, в случае, если не заполнено первое поле
def test_operation_4(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys('2')
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

    selenium.save_screenshot('test_operation_4.png')

    assert selenium.find_element(By.ID, 'answer').text == 'ERR', print('Тест провален')


# TEST_14
# проверка невыполнения операций, в случае, если не заполнено второе поле
def test_operation_5(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys('2')
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

    selenium.save_screenshot('test_operation_5.png')

    assert selenium.find_element(By.ID, 'answer').text == 'ERR', print('Тест провален')