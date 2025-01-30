from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scen_3():
    try:
        driver = webdriver.Chrome()
        start_time = time.time()  # Запускаем таймер

        # Открываем страницу /top
        driver.get("http://127.0.0.1:5000/top")
        driver.maximize_window()
        time.sleep(2)  # Даем время на загрузку

        # Нажимаем на кнопку /html/body/div[2]/div[1]/div[2]/a[2]
        button1 = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/a[2]")
        button1.click()
        time.sleep(2)  # Даем время загрузиться

        # Нажимаем на кнопку /html/body/div[2]/div[2]/button
        button2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/button")
        button2.click()
        time.sleep(2)  # Даем время на загрузку

        # Скроллим вниз немного
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Даем время прогрузиться

        # Находим имя движика
        engine_name = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/div[1]/h1").text
        print(f"Название движика: {engine_name}")

    finally:
        end_time = time.time()
        execution_time = end_time - start_time
        driver.quit()
        print(f"Время выполнения сценария: {execution_time:.2f} секунд")

scen_3()
