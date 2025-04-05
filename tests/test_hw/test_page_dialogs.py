from components.components import WebElement
from pages.modal_dialogs import ModalDialogs
import time
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert modal_dialogs.btns_second_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.home_icon.click()
    browser.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == "DEMOQA"
    browser.set_window_size(1000, 1000)


