import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store',default=None,help='select language es,en,ru or other')
@pytest.fixture(scope='function')
def browser(request):
    user_language=request.config.getoption('language')
    option=Options()
    option.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser=webdriver.Chrome(options=option)
    yield browser
    print('\nexit browser')
    browser.quit()