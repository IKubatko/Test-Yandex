import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestYandexRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://passport.yandex.ru/registration/")

    def test_registration(self):
        driver = self.driver
        assert "Регистрация" in self.driver.title

        firstname = driver.find_element_by_id("firstname")
        firstname.send_keys("Керк")

        lastname = self.driver.find_element_by_id("lastname")
        lastname.send_keys("Керк")

        login = self.driver.find_element_by_id("login")
        login.send_keys("Test9191919191")

        password = self.driver.find_element_by_id("password")
        password.send_keys("123456789qwerty")

        password_confirm = self.driver.find_element_by_id("password_confirm")
        password_confirm.send_keys("123456789qwerty")

        self.driver.find_element_by_xpath(
            '//form[@class="registration__form registration__form_desktop"]'
            '//div[@class="phone__confirm-wrapper"]//span[@role="button"]').click()

        self.driver.find_element_by_xpath(
            '//span[@data-t="user-question-all"]').click()

        self.driver.find_element_by_xpath(
            '//div[@class="menu menu_size_m menu_width_max menu_theme_normal '
            'menu_view_classic menu_type_radio select2__menu"]//div[2]').click()

        security_answer = self.driver.find_element_by_id("hint_answer")
        security_answer.send_keys("улица Булгакова")

        self.driver.find_element_by_xpath('//div[@class ="form__submit"]/button[1]').click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='error-message']")))
        error_message = self.driver.find_elements_by_xpath("//div[@class='error-message']")
        if error_message:
            error_message = error_message[0]
            print(error_message.text)
            assert error_message.text == "Необходимо ввести символы"


if __name__ == "__main__":
    unittest.main()
