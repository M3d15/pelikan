from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators

class BasePage():
    def __init__(self, browser, link, timeout=10):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def authorization(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        login_field = self.browser.find_element(*MainPageLocators.LOGIN_FIELD)
        login_field.send_keys("admin")

        pass_field = self.browser.find_element(*MainPageLocators.PASS_FIELD)
        pass_field.send_keys("1234567")

        button = self.browser.find_element(*MainPageLocators.BUTTON)
        button.click()

        user_name = self.browser.find_element(*MainPageLocators.USER_NAME).text

        assert "admin@admin.admin" in user_name, "Login isn't success"

    """
        def is_not_element_present(self, how, what, timeout=4):
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return True
            return False

        def is_disappeared(self, how, what, timeout=4):
            try:
                WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                    until_not(EC.presence_of_element_located((how, what)))
            except TimeoutException:
                return False
            return True
    """