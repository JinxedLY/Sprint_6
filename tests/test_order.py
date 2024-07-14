import allure
from conftest import driver
from pages.main_page import ScooterMainPage
from pages.order_page import ScooterOrderPage
from stuff.test_data import Answers


class TestOrder:
    @allure.title('Проверка возможности заказа с первым сетом данных при входе через хедер')
    @allure.description(
        'Входим через кнопку в хедере, передаем первого юзера, проверяем модалку на заказ')
    def test_order_first_user_from_header_with_second_user_success(self, driver):
        main_page = ScooterMainPage(driver)
        order_page = ScooterOrderPage(driver)
        user_data = Answers.user_1
        main_page.go_to_site()
        main_page.order_from_header()
        order_page.fill_first_step(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        order_page.next_step()
        order_page.fill_second_step(user_data[5])
        order_page.make_an_order()
        order_page.confirm_order()
        assert order_page.final_button_check()

    @allure.title('Проверка возможности заказа со вторым сетом данных при входе через тело')
    @allure.description(
        'Входим через кнопку в теле, передаем второго юзера, проверяем модалку на заказ')
    def test_order_first_user_from_body_with_second_user_success(self, driver):
        main_page = ScooterMainPage(driver)
        order_page = ScooterOrderPage(driver)
        user_data = Answers.user_2
        main_page.go_to_site()
        main_page.order_from_body()
        order_page.fill_first_step(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
        order_page.next_step()
        order_page.fill_second_step(user_data[5])
        order_page.make_an_order()
        order_page.confirm_order()
        assert order_page.final_button_check()
