
from pages.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver,self.base_url)
        self.btn_add=WebElement(driver,"#addNewRecordButton")
        self.btn_submit = WebElement(driver, "#submit")
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.user_age = WebElement(driver, "#age")
        self.user_salary = WebElement(driver, "#salary")
        self.user_departament = WebElement(driver, "#department")
        self.btn_pencil = WebElement(driver, "#edit-record-1")
        self.btn_delete = WebElement(driver,"#delete-record-1")
        self.firstname = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(1)")
        self.lastname = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div >  div:nth-child(2)")
        self.email = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(4)")
        self.salary = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(5)")
        self.departament = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-thead.-header > div > div:nth-child(6)")
        self.modal_form = WebElement(driver,"body > div.fade.modal.show > div > div")
        self.table = WebElement(driver,"#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody")