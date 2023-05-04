from selenium import webdriver
import pytest
import settings

#Фикстура с функцией открытия и закрытия браузера
@pytest.fixture()
def browser():
    print('Browser start...')
    browser = webdriver.Chrome('C:\Users\2668a\Документы\проект\chromedriver.exe')
    browser.implicitly_wait(5)
    browser.get(settings.BASE_URL)

    yield browser

    print('Browser quit...')
    browser.quit()

