from pages.modal_dialogs import ModalDialogs
import time
def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    assert not modal_dialogs.alert()
    modal_dialogs.smallModal.click()
    time.sleep(2)
    modal_dialogs.smallModal_btn.click()
    time.sleep(2)
    modal_dialogs.largeModal.click()
    time.sleep(2)
    modal_dialogs.largeModal_btn.click()
