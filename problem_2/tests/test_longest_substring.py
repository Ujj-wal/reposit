from pages.home_page import HomePage
from pages.result_page import ResultPage
from utils.browser_setup import init_browser
import time

def test_longest_substring_result():
    driver = init_browser()
    driver.get("https://agrichain.com")
    driver.maximize_window()
    time.sleep(1)

    home_page = HomePage(driver)
    home_page.enter_text("abcabcbb")
    home_page.click_submit()
    time.sleep(2)

    result_page = ResultPage(driver)
    output_text = result_page.fetch_result()
    assert output_text == "abc"

    driver.quit()
