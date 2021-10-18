from selenium import webdriver
import pytest
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(url='http://selenium1py.pythonanywhere.com/' + language + '/catalogue/coders-at-work_207/')
    yield browser
    time.sleep(5)
    browser.quit()
