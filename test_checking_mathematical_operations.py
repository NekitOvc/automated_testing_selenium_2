"""Основные математические операции"""
from test_options import testing, get_chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

import time
import requests


# TEST_01
# проверка, что пользователь может успешно перейти на сайт
def test_opening_page(testing):
    selenium = testing
    # открытие сайта
    url = 'https://testpages.herokuapp.com/styled/calculator'
    selenium.get(url)
    response = requests.get(url)

    selenium.save_screenshot('test_opening_page.png')

    try:
        element = WebDriverWait(selenium, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        print('Элемент отобразился')
    except:
        print('Элемент h1 не отобразился!')

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Simple Calculator', print('Тест провален')
    assert response.status_code == 200, print('Тест провален')


# TEST_02
# проверка операции сложения при введенных данных в диапазоне от -100 до 100
def test_addition_operation(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
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

    selenium.save_screenshot('test_addition_operation.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_03
# проверка операции вычитания при введенных данных в диапазоне от -100 до 100
def test_subtraction_operation(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
    answer = str(number1 - number2)

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

    selenium.save_screenshot('test_subtraction_operation.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_04
# проверка операции умножения при введенных данных в диапазоне от -100 до 100
def test_multiplication_operation(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
    answer = str(number1 * number2)

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

    selenium.save_screenshot('test_multiplication_operation.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')


# TEST_05
# проверка операции деления при введенных данных в диапазоне от -100 до 100
def test_division_operation(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://testpages.herokuapp.com/styled/calculator')

    try:
        element = WebDriverWait(selenium, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="calculate"]')))
        print('Элемент отобразился')
    except:
        print('Элемент XPATH не отобразился!')

    number1 = randint(-100, 100)
    number2 = randint(-100, 100)
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

    selenium.save_screenshot('test_division_operation.png')

    assert selenium.find_element(By.ID, 'answer').text == answer, print('Тест провален')
