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
#