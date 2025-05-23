from components.components import WebElement
from pages.base_page import BasePage
class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url= "https://demoqa.com/alerts"
        super().__init__(driver, self.base_url)
        self.alertButton = WebElement(driver, "#alertButton")
        self.confirmButton = WebElement(driver, "#confirmButton")
        self.confirmResult= WebElement(driver, "#confirmResult")
        self.promptButton = WebElement(driver, "#promtButton")
        self.promptResult = WebElement(driver, "#promptResult")
