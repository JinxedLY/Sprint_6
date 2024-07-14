import allure
import time
from stuff.pathways import Pathways
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть сайт')
    def go_to_site(self):
        return self.driver.get(Pathways.base_path)

    @allure.step('Ждем пока элемент прогрузится')
    def wait_thing(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Клик по элементу')
    def click_thing(self, locator):
        element = self.wait_thing(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(1)
        element.click()

    @allure.step('Считать текст элемента')
    def read_thing(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Скролл до элемента')
    def scroll_to_locator(self, locator):
        element = self.wait_thing(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на новую вкладку')
    def switch_to_the_new_tab(self):  # Переключить на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

