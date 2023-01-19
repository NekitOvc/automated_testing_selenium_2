"""Математические операции, где точка является разделителем между целой и дробной частью числа"""

from test_options import testing, get_chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random


# TEST_07
# проверка операции сложения десятичных дробей при введенных данных в диапазоне от 0.1 до 100.1
# точка является разделителем между целой и дробной частью числа
def test_adding_decimals(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = round(random.uniform(0.1, 100.1), 2)
    number2 = round(random.uniform(0.1, 100.1), 2)
    answer = str(number1 + number2)

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys(number1)
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys(number2)
    time.sleep(1)
    # нажать на выбор операции
    selenium.find_element(By.ID, 'function').click()
    time.sleep(1)
    # выбрать операцию сложения
    selenium.find_element(By.XPATH, '//*[@id="function"]/option[1]').click()
    time.sleep(2)
    # нажать Calculate
    selenium.find_element(By.XPATH, '//*[@id="calculate"]').click()
    time.sleep(2)

    selenium.save_screenshot('test_adding_decimals.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_08
# проверка операции вычитания десятичных дробей при введенных данных в диапазоне от 0.1 до 100.1
# точка является разделителем между целой и дробной частью числа
def test_subtracting_decimals(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = round(random.uniform(0.1, 100.1), 2)
    number2 = round(random.uniform(0.1, 100.1), 2)
    answer = str(round(number1 - number2, 2))

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys(number1)
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys(number2)
    time.sleep(1)
    # нажать на выбор операции
    selenium.find_element(By.ID, 'function').click()
    time.sleep(1)
    # выбрать операцию вычитания
    selenium.find_element(By.XPATH, '//*[@id="function"]/option[3]').click()
    time.sleep(2)
    # нажать Calculate
    selenium.find_element(By.XPATH, '//*[@id="calculate"]').click()
    time.sleep(2)

    selenium.save_screenshot('test_subtracting_decimals.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_09
# проверка операции умножения десятичных дробей при введенных данных в диапазоне от 0.1 до 100.1
# точка является разделителем между целой и дробной частью числа
def test_multiplication_decimals(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = round(random.uniform(0.1, 100.1), 2)
    number2 = round(random.uniform(0.1, 100.1), 2)
    answer = str(round(number1 * number2, 4))

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys(number1)
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys(number2)
    time.sleep(1)
    # нажать на выбор операции
    selenium.find_element(By.ID, 'function').click()
    time.sleep(1)
    # выбрать операцию умножения
    selenium.find_element(By.XPATH, '//*[@id="function"]/option[2]').click()
    time.sleep(2)
    # нажать Calculate
    selenium.find_element(By.XPATH, '//*[@id="calculate"]').click()
    time.sleep(2)

    selenium.save_screenshot('test_multiplication_decimals.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_10
# проверка операции деления десятичных дробей при введенных данных в диапазоне от 0.1 до 100.1
# точка является разделителем между целой и дробной частью числа
def test_division_decimals(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = round(random.uniform(0.1, 100.1), 2)
    number2 = round(random.uniform(0.1, 100.1), 2)
    answer = str(round(number1 / number2, 6))

    # ввод данных в первое поле
    selenium.find_element(By.ID, 'number1').send_keys(number1)
    time.sleep(1)
    # ввод данных во второе поле
    selenium.find_element(By.ID, 'number2').send_keys(number2)
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

    selenium.save_screenshot('test_division_decimals.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')