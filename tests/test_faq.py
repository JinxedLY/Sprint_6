import allure
import pytest
from conftest import driver
from pages.main_page import ScooterMainPage
from stuff.test_data import Answers
from locators.main_loc import MainPageLoc


class TestFaq:
    @allure.title('Проверка заполнения аккордеона ЧаВо')
    @allure.description('Проверка что в разделе "О важном" ответы на вопросы отображаются и совпадают с ожидаемыми')
    @pytest.mark.parametrize('question_number, expected_answer', Answers.answers)
    def test_click_faq_question_and_compare_answer_to_expected_value_match_success(self, driver, question_number, expected_answer):
        main_page = ScooterMainPage(driver)
        main_page.go_to_site()
        main_page.cookie_click()
        main_page.scroll_to_faq(MainPageLoc.question[question_number])
        actual_text = main_page.get_faq_answer(MainPageLoc.question[question_number], MainPageLoc.answer[question_number])
        assert actual_text == expected_answer
