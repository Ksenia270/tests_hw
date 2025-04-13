from pages.links import WindowTab
import time
def test_window_tab(browser):
    window_tab = WindowTab(browser)
    window_tab.visit()
    assert window_tab.new_tab.get_text() == "Home"
    assert window_tab.new_tab.get_dom_attribute("href") == "https://demoqa.com"


    assert len(browser.window_handles) == 1
    window_tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
