from pages.text_box import TextBox
from components.components import WebElement
def test_text_box_sumbit(browser):
    text_box = TextBox(browser)
    text_box.visit()
    assert text_box.btn_submit.check_css("color", "rgba(255, 255, 255, 1)")
    assert text_box.btn_submit.check_css("backgrondColor", "rgba(0, 123, 255, 1)")
    assert text_box.btn_submit.check_css("borderColor", "rgb(0,123,255)")
