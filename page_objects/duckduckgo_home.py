from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoHome:

    SEARCH_FIELD = (By.NAME, 'q')

    def __init__(self, browser):
        self._browser = browser

    def search(self, term):
        # the *self.SEARCH_FIELD unpacks the tuple and passes in
        # data within. that is, the * let's us do 
        # find_element(By.NAME, 'q')
        # and not
        # find_element((By.NAME, 'q'))
        element = self._browser.find_element(*self.SEARCH_FIELD)
        element.send_keys(term + Keys.RETURN)


