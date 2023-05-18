from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_result = '//h4[@class="results"]'
        self.search_option = "Supply Chain"
        self.supply_chain = "resource-title"
        self.wait = WebDriverWait(driver, 10)

    def result_displayed(self):
        result = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.search_result))
        ).text
        return result

    def option_selection(self):
        self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.search_option))
        ).click()
        option_text = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.supply_chain))
        ).text
        return option_text
