
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.demoblaze.com/")  # Открываем сайт https://www.demoblaze.com/

    def samsung_click(self):
        samsung_galaxy_s6 = self.driver.find_element(By.XPATH, "//a[@href='prod.html?idp_=1']")  # Ищем элемент по XPATH и сохраняем его значение
        samsung_galaxy_s6.click()  # Кликаем по найденному элементу

    def monitor_elements(self):
        monitors = self.driver.find_element(By.XPATH, """//a[@onclick = "byCat('monitor')"]""")  # Ищем элемент по XPATH и сохраняем его значение
        monitors.click()  # Кликаем по найденному элементу

    def count_elements(self, count_):
        value = self.driver.find_elements(By.CSS_SELECTOR, "div[class^=col-lg-4]")  # Ищем элементЫ по CSS-селектору и сохраняем ИХ значения в списке
        assert len(value) == count_  # Проверяем, что элементов (длина списка) равна 2