import pytest
import allure

from main_page import MainPage
from selenium import webdriver

# Настройки для UI тестов
UI_BASE_URL = "https://www.chitai-gorod.ru/"

# Тестовые данные
SEARCH_TERMS = {
    "cyrillic": "книга",
    "latin": "book",
    "numbers": "1984",
    "dash": "книга-приключение",
    "exclamation": "книга!",
    "question": "книга?",
}


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@allure.step("Тест: Поле принимает кириллицу")
def test_search_cyrillic(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['cyrillic'])
    assert entered_text == SEARCH_TERMS['cyrillic'], f"Ожидали '{
        SEARCH_TERMS['cyrillic']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает латиницу")
def test_search_latin(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['latin'])
    assert entered_text == SEARCH_TERMS['latin'], f"Ожидали '{
        SEARCH_TERMS['latin']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает цифры")
def test_search_numbers(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['numbers'])
    assert entered_text == SEARCH_TERMS['numbers'], f"Ожидали '{
        SEARCH_TERMS['numbers']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает дефис")
def test_search_dash(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['dash'])
    assert entered_text == SEARCH_TERMS['dash'], f"Ожидали '{
        SEARCH_TERMS['dash']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает восклицательный знак")
def test_search_exclamation(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['exclamation'])
    assert entered_text == SEARCH_TERMS['exclamation'], f"Ожидали '{
        SEARCH_TERMS['exclamation']}', но получили '{entered_text}'"


@allure.step("Тест: Поле принимает вопросительный знак")
def test_search_question(main_page):
    entered_text = main_page.enter_search_text(SEARCH_TERMS['question'])
    assert entered_text == SEARCH_TERMS['question'], f"Ожидали '{
        SEARCH_TERMS['question']}', но получили '{entered_text}'"