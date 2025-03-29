from selenium import webdriver
from selenium.webdriver.common.by import By
from components.components import FooterComponent
from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_footer_text(browser):

    browser.get('https://demoqa.com/')
    footer = FooterComponent(browser)
    assert footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
def test_elements_page_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page=ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
