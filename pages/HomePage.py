from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_expand_btn = '//*[@id="open-global-search"]'
        self.search_box = "site-search-keyword"
        self.search_btn = '//*[@id="global-site-search"]/form/button/i'

        self.search_result = '//h4[@class="results"]'
        self.search_option = "Supply Chain"
        self.supply_chain = "resource-title"
        self.wait = WebDriverWait(driver, 10)

    def search_click(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.search_expand_btn))
        ).click()

    def search_keyword(self, keyword):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.search_box))).send_keys(
            keyword
        )
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_btn))).click()
