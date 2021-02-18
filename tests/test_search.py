from page_objects.duckduckgo_home import DuckDuckGoHome

class TestSearch:

    # the browser variable comes from the fixture in conftest.py
    def test(self, browser):
        ddg_home = DuckDuckGoHome(browser)
        browser.get('http://www.duckduckgo.com')

        ddg_home.search('google sux')


