from selenium.webdriver.common.by import By


class OrderPageLoc:

    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    lastname_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    station_suggest = (By.XPATH, ".//div[text() = 'Алексеевская']")
    phone_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    continue_button = (By.XPATH, "//button[text()='Далее']")
    when_field = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    duration_field = (By.XPATH, '//input[@placeholder="* Срок аренды"]')
    duration_value = (By.XPATH, ".//div[text() = 'сутки']")
    order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons__")]//button[text()="Заказать"]')
