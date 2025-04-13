from pages.webtables import WebTables
from components.components import WebElement
import time
def test_sort(browser):
    web_tables = WebTables(browser)
    web_tables.visit()
    web_tables.firstname.click_force()
    time.sleep(2)
    web_tables.lastname.click_force()
    time.sleep(2)
    web_tables.email.click_force()
    time.sleep(2)
    web_tables.salary.click_force()
    time.sleep(2)
    web_tables.departament.click_force()
    time.sleep(2)