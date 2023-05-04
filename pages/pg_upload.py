from selenium.webdriver.common.by import By
from pages.base import BasePage
from utils.dir_file_utils import *


class UploadPage(BasePage):
    page_url = "https://demo.guru99.com/test/upload/"

    UPLOAD_FIELD_ID = "uploadfile_0"
    TERM_CHECK_BOX_CSS = ".field_check"
    SUBMIT_BUTTON = "submitbutton"
    UPLOAD_FIELD_TITLE_XPATH = "//b[contains(text(), 'Select file to send(max 196.45 MB)')]"
    RESULT_MESSAGE_CSS = "#res center"

    def is_loaded(self):
        return self.have_element_displayed(By.XPATH, self.UPLOAD_FIELD_TITLE_XPATH)

    def upload_file(self, file_name):
        input_file_field = self.wait_for_element_visible(By.ID, self.UPLOAD_FIELD_ID)
        input_file_field.send_keys(default_file_path_to_upload() + file_name)

    def click_check_box(self):
        self.wait_for_element_visible(By.CSS_SELECTOR, self.TERM_CHECK_BOX_CSS).click()

    def click_submit_button(self):
        self.wait_for_element_visible(By.ID, self.SUBMIT_BUTTON).click()

    def get_upload_result_msg(self):
        return self.wait_for_element_visible(By.CSS_SELECTOR, self.RESULT_MESSAGE_CSS).text
