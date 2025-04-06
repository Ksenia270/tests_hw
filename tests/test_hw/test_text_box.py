from pages.text_box import TextBox
import time
def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.name.send_keys("tester")
    time.sleep(2)
    text_box.current_address.send_keys("test")
    time.sleep(2)
    text_box.btn_submit.click_force()
