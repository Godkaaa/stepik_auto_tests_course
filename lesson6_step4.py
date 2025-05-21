from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # Ссылка на тестируемую страницу
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Уникальные селекторы для обязательных полей формы
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input")
    email.send_keys("ivan.petrov@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждём загрузки новой страницы
    time.sleep(1)

    # Проверяем, что регистрация прошла успешно
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Пауза, чтобы можно было увидеть результат в браузере
    time.sleep(10)
    browser.quit()
