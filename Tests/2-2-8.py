from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Ivan")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Petrov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email")

    addFile = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    addFile.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    