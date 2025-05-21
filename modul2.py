from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока в элементе с id='price' появится текст '$100'
    wait = WebDriverWait(browser, 15)  # 15 секунд, чтобы хватило по условию
    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажать кнопку Book
    browser.find_element(By.ID, "book").click()

    # Решаем капчу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Отправляем ответ
    browser.find_element(By.ID, "solve").click()

    # Ждем и получаем текст из алерта
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)  # Это число-ответ
    alert.accept()

finally:
    browser.quit()
