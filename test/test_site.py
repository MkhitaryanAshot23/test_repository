import time
from pages.homepage import Homepage
from pages.product import Product


def test_samsung_galaxy_s6(driver):
    home_page = Homepage(driver)
    home_page.open()
    home_page.samsung_click()
    product_page = Product(driver)
    product_page.check_title_is("Samsung galaxy s6")


def test_monitors(driver):
    home_page = Homepage(driver)
    home_page.open()
    home_page.monitor_elements()
    time.sleep(3)  # Ждем 3 секунды
    home_page.count_elements(2)

