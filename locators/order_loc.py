from selenium.webdriver.common.by import By


class OrderPageLocFirstStep:

    name_field = (By.XPATH, '//input[@placeholder="* Имя"]')
    lastname_field = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_field = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ]')
    station_field = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    phone_field = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    continue_button = (By.XPATH, "//button[text()='Далее']")
    when_field = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    duration_field = (By.XPATH, '//input[@placeholder="* Срок аренды"]')
    order_button = (By.XPATH, '//div[contains(@class, "Order_Buttons__")]//button[text()="Заказать"]')
