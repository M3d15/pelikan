from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".container.nav-wrapper .right>li>a")
    LOGIN_FIELD = (By.CSS_SELECTOR, "[name='username']")
    PASS_FIELD = (By.CSS_SELECTOR, "[name='password']")
    BUTTON = (By.CSS_SELECTOR, ".btn[type='submit']")
    USER_NAME = (By.CSS_SELECTOR, ".right .dropdown-trigger")
