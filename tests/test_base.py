import allure
from conftest import driver
from pages.main_page import ScooterMainPage
from stuff.pathways import Pathways

class TestNavigation:
    @allure.title('Проверка навигации при клике на лого яндекса')
    @allure.description('Кликаем на лого яндекса и проверяем оказались ли мы на странице дзена')
    def test_click_yandex_logo_redirect_to_dzen_success(self, driver):
        main_page = ScooterMainPage(driver)
        main_page.go_to_site()
        main_page.poke_yandex()
        main_page.switch_to_the_new_tab()
        assert main_page.dzen_button_check()

    @allure.title('Проверка навигации при клике на лого самоката')
    @allure.description('Уходим с главной страницы, кликаем на лого самоката и проверяем оказались ли мы на главной странице')
    def test_click_scooter_logo_redirect_to_base_path_success(self, driver):
        main_page = ScooterMainPage(driver)
        main_page.go_to_site()
        main_page.order_from_header()
        main_page.poke_scooter()
        assert driver.current_url == Pathways.base_path
