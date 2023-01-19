import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math



@pytest.mark.parametrize('number', ["236895", "236896","236897","236898","236899","236903","236904","236905"])
def test_pages_with_authorization(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    header = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "ember33"))
    )

    loginButton = browser.find_element(By.ID, "ember33")
    loginButton.click()

    """ emailField = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth_login"))
    ) """

        # Ваш код, который заполняет обязательные поля
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("*****")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("*****")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button.click()

    popup = WebDriverWait(browser, 4).until(
        EC.invisibility_of_element((By.ID, "ember101"))
    )

    time.sleep(3)

    answer = math.log(int(time.time()))

    result = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
    #time.sleep(3)
    
    #result.send_keys(answer)
    # Отправляем заполненную форму
    """ button2 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
    ) """
    #time.sleep(1)
    
    #button2.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    assert welcome_text == "Correct!"
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
