from pages.webtables import WebTables
import time
def test_webtables(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    assert web_tables.btn_add.get_text() == "Add"

    web_tables.btn_add.click()
    time.sleep(2)
    web_tables.btn_submit.click_force()
    assert web_tables.modal_form.visible()
    time.sleep(2)
    web_tables.first_name.send_keys("tester")
    web_tables.last_name.send_keys("testerovich")
    web_tables.user_email.send_keys("test@mail.ru")
    web_tables.user_age.send_keys("40")
    web_tables.user_salary.send_keys("5000")
    web_tables.user_departament.send_keys("IT")
    time.sleep(2)
    web_tables.btn_submit.click()
    time.sleep(2)
    assert not web_tables.modal_form.visible()
    web_tables.btn_pencil.click()
    web_tables.first_name.clear()
    web_tables.first_name.send_keys("Kate")
    time.sleep(2)
    web_tables.btn_submit.click()
    time.sleep(2)
    web_tables.btn_delete.click()
    time.sleep(2)

