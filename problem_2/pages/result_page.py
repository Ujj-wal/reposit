class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.result_label = "span#result"

    def fetch_result(self):
        return self.driver.find_element("css selector", self.result_label).text
