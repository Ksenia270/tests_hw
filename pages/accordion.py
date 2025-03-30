from pages.base_page import BasePage
from components.components import WebElement
class Accordion(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)
        self.text = WebElement(driver, '#section1Content > p')
        self.heading = WebElement(driver, "#section1Heading")
        self.section = WebElement(driver,'#section2Content > p:nth-child(1)')
        self.section_second= WebElement(driver,'#section2Content > p:nth-child(2)')
        self.section_third= WebElement(driver, '#section3Content > p')

#
#             SECTION2_CONTENT_1 = (By.CSS_SELECTOR, '#section2Content > p:nth-child(1)')
#             SECTION2_CONTENT_2 = (By.CSS_SELECTOR, '#section2Content > p:nth-child(2)')
#             SECTION3_CONTENT = (By.CSS_SELECTOR, '#section3Content > p')
#         self.text
#     def section1_heading(self):
#                 return self.browser.find_element(*self.SECTION1_HEADING)
#
#             def section1_content(self):
#                 return self.browser.find_element(*self.SECTION1_CONTENT)
#
#             def section2_content_1(self):
#                 return self.browser.find_element(*self.SECTION2_CONTENT_1)
#
#             def section2_content_2(self):
#                 return self.browser.find_element(*self.SECTION2_CONTENT_2)
#
#             def section3_content(self):
#                 return self.browser.find_element(*self.SECTION3_CONTENT)
#
#             def click_section1_heading(self):
#                 self.section1_heading().click()