from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element(By.ID, "num1")
    x = number_1.text
    print(x)

    number_2 = browser.find_element(By.ID, "num2")
    y = number_2.text
    print(y)

    numb =int(x) + int(y)
    print(numb)
    

    from selenium.webdriver.support.select import Select
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(str(numb))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    