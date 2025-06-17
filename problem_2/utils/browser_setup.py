from selenium import webdriver

def init_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)
