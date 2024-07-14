import allure
import pytest
from conftest import driver
from stuff.test_data import Answers
from pages.main_page import ScooterMainPage
from pages.order_page import ScooterOrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestOrder:
    @allure.title('Проверка возможности заказа с первым сетом данных при входе через хедер')
    @allure.description(
        'Входим через кнопку в хедере, передаем первого юзера, проверяем модалку на заказ')
    def test_order_first_user_from_header_with_navigation_success(self, driver):
        main_page = ScooterMainPage(driver)
        order_page = ScooterOrderPage(driver)
        user_data = Answers.user_1
        main_page.go_to_site()
        main_page.order_from_header()
        order_page.fill_first_step(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        order_page.next_step()
        order_page.fill_second_step(user_data[5])
        order_page.make_an_order()
