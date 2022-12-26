from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstName = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        firstName.send_keys("Ivan")
        lastName = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        lastName.send_keys("Petrov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text not visible")
        
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        firstName = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        firstName.send_keys("Ivan")
        lastName = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        lastName.send_keys("Petrov")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        email.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome text not visible")
        
if __name__ == "__main__":
    unittest.main()
