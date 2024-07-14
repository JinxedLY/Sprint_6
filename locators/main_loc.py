from selenium.webdriver.common.by import By


class MainPageLoc:

    order_button_body = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    order_button_head = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    accept_cookie_button = (By.ID, 'rcc-confirm-button')

    question = {
        1: (By.ID, "accordion__heading-0"),
        2: (By.ID, "accordion__heading-1"),
        3: (By.ID, "accordion__heading-2"),
        4: (By.ID, "accordion__heading-3"),
        5: (By.ID, "accordion__heading-4"),
        6: (By.ID, "accordion__heading-5"),
        7: (By.ID, "accordion__heading-6"),
        8: (By.ID, "accordion__heading-7")
    }

    answer = {
        1: (By.ID, "accordion__panel-0"),
        2: (By.ID, "accordion__panel-1"),
        3: (By.ID, "accordion__panel-2"),
        4: (By.ID, "accordion__panel-3"),
        5: (By.ID, "accordion__panel-4"),
        6: (By.ID, "accordion__panel-5"),
        7: (By.ID, "accordion__panel-6"),
        8: (By.ID, "accordion__panel-7")
    }