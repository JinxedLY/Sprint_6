import allure
from locators.main_loc import MainPageLoc
from pages.base_page import BasePage


class ScooterMainPage(BasePage):
    @allure.step('Принимаем условия работы с куками')
    def cookie_click(self):
        self.click_thing(MainPageLoc.accept_cookie_button)

    @allure.step('Скролл до чавошки')
    def scroll_to_faq(self, question):
        self.scroll_to_locator(question)

    @allure.step('Клик по вопросу чавошки')
    def click_on_question(self, question):
        self.click_thing(question)

    @allure.step('Считать ответ чавошки')
    def get_faq_answer(self, question, answer):
        self.click_on_question(question)
        return self.read_thing(answer)

    @allure.step('Клац по кнопке заказа в шапке')
    def order_from_header(self):
        self.click_thing(MainPageLoc.order_button_head)

    @allure.step('Клац по кнопке заказа в теле')
    def order_from_body(self):
        self.click_thing(MainPageLoc.order_button_body)
