# В этот файл мы выносим функцию с декоратором @pytest.fixture()
# У файла должно быть название conftest.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Этот модуль позволяет запускать тесты в безголовом режиме (без запуска браузера)
import pytest


@pytest.fixture()
def driver():
    options = Options()  # Создаем экземпляр класса Options
    options.add_argument('--headless')  # Добавляем экземпляру класса значение --headless
    driver = webdriver.Chrome(options=options)  # Открываем браузер Chrome в безголовом режиме
    driver.maximize_window()     # Разворачиваем окно браузера полностью
    driver.implicitly_wait(3)    # Ищем элементы на странице в течение 3 секунд
    yield driver  # Возвращаем переменную driver, которая хранит объект webdriver.Chrome().
                  # Начинается выполнение какого-то метода с переменной driver в качестве параметра
