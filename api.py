import sys
import os
import pytest
import requests
import allure


API_BASE_URL = "https://web-gate.chitai-gorod.ru/api/v2/search/facet-search?customerCityId=213&phrase="
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3MzM3ODIsImlhdCI6MTczMzU2NTc4MiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjY2NmE0NWY0NDhmOWYwZmFmZmRkODFlZjYyODg0Y2E5ZGZhOGVmMmY1YzBjMTRiMjc1MDliYTI2NTgxMDRmZDciLCJ0eXBlIjoxMH0.aEQvRYs-_Dj1NTr-pK4Xbr_4LXmcrHSG0zMVyim9J3s"
HEADERS = {
    "Authorization": AUTH_TOKEN}

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def log_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {response.json()}")
    except requests.exceptions.JSONDecodeError:
        print("Response content is not JSON")


@pytest.fixture
def session():
    """Фикстура для создания сессии, которая будет использоваться в тестах."""
    with requests.Session() as session:
        session.headers.update(HEADERS)
        yield session


@pytest.mark.parametrize("title",
                         ["Война и мир",
                          "Гарри Поттер",
                          "книга-приключение"])
@allure.story("Поиск книг по названию")
def test_search_by_title(session, title):
    with allure.step(f"Поиск книги с названием '{title}'"):
        response = session.get(f"{API_BASE_URL}{title}")
        log_response(response)
        assert response.status_code == 200, f"Expected 200, but got {
            response.status_code}"
        json_response = response.json()
        assert "data" in json_response, f"No 'data' key found for title: {title}"
        assert len(json_response["data"]
                   ) > 0, f"No books found for title: {title}"