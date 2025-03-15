from selenium.webdriver.common.by import By
from selenium import webdriver


class Product:

    def __init__(self, driver):
        self.driver = driver

    def check_title_is(self, title):
        value = self.driver.find_element(By.XPATH, "//h2[text() = 'Samsung galaxy s6']")  # Ищем элемент по XPATH и сохраняем его значение
        assert value.text == title  # Преобразуем найденный элемент в текстовой формат и сравниваем его с текстом "Samsung galaxy s6"
