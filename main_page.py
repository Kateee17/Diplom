from selenium.webdriver.common.by import By
import allure


class MainPage:
    URL = "https://www.chitai-gorod.ru/"
    SEARCH_INPUT = (By.CLASS_NAME, "header-search__input")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем главную страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Ввод текста '{text}' в поле поиска")
    def enter_search_text(self, text):
        search_field = self.driver.find_element(*self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        search_field.submit()
        return search_field.get_attribute("value")