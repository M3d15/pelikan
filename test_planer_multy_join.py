from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://v5t.pelikan.online/"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".container.nav-wrapper .right").click()
    
    find_login_field = browser.find_element(By.CSS_SELECTOR, "[name='username']")
    find_login_field.send_keys("admin")

    find_pass_field = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    find_pass_field.send_keys("1234567")
    
    browser.find_element(By.CSS_SELECTOR, ".btn[type='submit']").click()

    find_user_name = browser.find_element(By.CSS_SELECTOR, ".right .dropdown-trigger")
    text_user_name = find_user_name.text

    #assert "admin@admin.admin" in text_user_name, "Login isn't success"

    browser.find_element(By.CSS_SELECTOR, "[data-href='/events/join/133/']").click()

    """
    # переключение на модальное окно и принятие сообщения
    confirm = browser.switch_to.alert.accept()
  
    # поиск Х 
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text 
    
    # вычисление Х и преобразование результата в строку
    res_x = calc(x)
    str_res = str(res_x)

    # поиск и заполнение поля ввода ответа
    find_answer = browser.find_element_by_id("answer")
    find_answer.send_keys(str_res)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    """
finally:
    #pass
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
