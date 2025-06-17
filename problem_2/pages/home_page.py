class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.text_input = "input#text"
        self.submit_button = "button#submit"

    def enter_text(self, text):
        self.driver.find_element("css selector", self.text_input).send_keys(text)

    def click_submit(self):
        self.driver.find_element("css selector", self.submit_button).click()
