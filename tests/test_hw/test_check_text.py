from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import FooterComponent

def test_footer_text(browser):
    browser.get('https://demoqa.com/')
    footer = FooterComponent(browser)
    assert footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text_please(browser):
    demo_qa_page = DemoQa(browser)
    elements_page=ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elements_page.text_please.get_text()=='Please select an item from left to start practice.'
def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()

