import pytest
import time
from pages.pg_upload import *
from config.base_config import *


@pytest.mark.usefixtures('driver')
class TestUploadGuru(object):

    def test_upload_a_valid_file(self, driver):
        upload_page = UploadPage(driver)
        driver.get(upload_page.page_url)
        assert upload_page.is_loaded()
        upload_page.upload_file(small_file_upload)
        upload_page.click_check_box()
        upload_page.click_submit_button()
        assert upload_page.get_upload_result_msg() == "1 file\nhas been successfully uploaded."

    def test_submit_without_file_upload(self, driver):
        upload_page = UploadPage(driver)
        driver.get(upload_page.page_url)
        assert upload_page.is_loaded()
        upload_page.click_submit_button()
        assert upload_page.get_upload_result_msg() == "Please upload file before submitting..."


