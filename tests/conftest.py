from selenium import webdriver
import pytest

# pass the method name into a test's arguements to call this
# and open firefox (or whatever browsers get added)
@pytest.fixture(autouse=True)
def browser():
    pytest.browser = webdriver.Firefox()
    yield pytest.browser
    pytest.browser.quit()
