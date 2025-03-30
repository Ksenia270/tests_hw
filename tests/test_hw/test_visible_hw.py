from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert  accordion.text.visible()
    accordion.heading.click()
    time.sleep(2)
def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.section.visible()
    assert not accordion.section_second.visible()
    assert not accordion.section_third.visible()


