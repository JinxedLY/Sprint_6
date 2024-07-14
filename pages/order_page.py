import allure
from locators.order_loc import OrderPageLoc
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class ScooterOrderPage(BasePage):

    @allure.step('Заполняем поле ввода "Имя"')
    def fill_name(self, name):
        self.send_keys(OrderPageLoc.name_field, name)

    @allure.step('Заполняем поле ввода "Фамилия"')
    def fill_lastname(self, lastname):
        self.send_keys(OrderPageLoc.lastname_field, lastname)

    @allure.step('Заполняем поле ввода "Адрес"')
    def fill_address(self, address):
        self.send_keys(OrderPageLoc.address_field, address)

    @allure.step('Заполняем поле ввода "Метро"')
    def fill_station(self, station):
        self.click_thing(OrderPageLoc.station_field)
        self.send_keys(OrderPageLoc.station_field, station)
        self.click_thing(OrderPageLoc.station_suggest)

    @allure.step('Заполняем поле ввода "Номер"')
    def fill_phone(self, phone):
        self.send_keys(OrderPageLoc.phone_field, phone)

    @allure.step('Заполняет поля ввода первого этапа заказа')
    def fill_first_step(self, name, lastname, address, station, phone):
        self.fill_name(name)
        self.fill_lastname(lastname)
        self.fill_address(address)
        self.fill_station(station)
        self.fill_phone(phone)

    @allure.step('Клац по кнопке продолжения')
    def next_step(self):
        self.click_thing(OrderPageLoc.continue_button)

    @allure.step('Заполняем поле ввода "Когда привезти самокат"')
    def fill_when(self, when):
        self.click_thing(OrderPageLoc.when_field)
        self.send_keys(OrderPageLoc.when_field, when)
        self.send_keys(OrderPageLoc.when_field, Keys.RETURN)

    @allure.step('Заполняем поле ввода "Срок аренды"')
    def fill_duration(self):
        self.click_thing(OrderPageLoc.duration_field)
        self.click_thing(OrderPageLoc.duration_value)

    @allure.step('Заполняем поля ввода второго этапа заказа')
    def fill_second_step(self, date):
        self.fill_when(date)
        self.fill_duration()

    @allure.step('Клац по кнопке создания заказа')
    def make_an_order(self):
        self.click_thing(OrderPageLoc.order_button)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.click_thing(OrderPageLoc.confirm_button)

    @allure.step('Проверка наличии кнопки проверки статуса заказа')
    def final_button_check(self):
        return self.wait_thing(OrderPageLoc.check_status_button).is_displayed()
