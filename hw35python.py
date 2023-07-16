

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def pogoda():
    browzer = webdriver.Edge()
    browzer.get('https://www.google.com')
    elem1 = browzer.find_element(By.ID, "APjFqb")
    elem2 = browzer.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")  # нашли кнопку поиск
    elem1.send_keys('погода Псков')
    elem2.click()
    time.sleep(5)
    browzer.close()


def cats():
    browzer = webdriver.Edge()
    browzer.get('https://www.google.com')
    elem1 = browzer.find_element(By.ID, "APjFqb")
    elem2 = browzer.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")  # нашли кнопку поиск
    elem1.send_keys('картинки котов')
    elem2.click()
    time.sleep(5)
    browzer.close()
def maps():
    browzer = webdriver.Edge()
    browzer.get('https://ya.ru/?utm_referrer=https%3A%2F%2Fyandex.ru%2F&ysclid=lk07xlhjec48421034')
    elem1 = browzer.find_element(By.ID, "text")
    elem2 = browzer.find_element(By.XPATH, "/html/body/main/div[2]/form/div[2]/button")  # нашли кнопку поиск
    elem1.send_keys('карта города')
    elem2.click()
    time.sleep(5)
    browzer.close()
def sez():
    browzer = webdriver.Edge()
    browzer.get('https://www.google.com')
    elem1 = browzer.find_element(By.ID, "APjFqb")
    elem2 = browzer.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")  # нашли кнопку поиск
    elem1.send_keys('особая экономическая зона псков')
    elem2.click()
    time.sleep(5)
    browzer.close()

while True:
    print("Меню:")
    print("1. Посмотреть погоду")
    print("2. Картинки котов")
    print("3. Карта города")
    print("4. Особая экономическая зона Псков")
    print("5. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        pogoda()
    elif choice == "2":
        cats()
    elif choice == "3":
        maps()
    elif choice == "4":
        sez()
    elif choice == "5":
        break
    else:
        print("ОШИБКА. Пожалуйста, выберите пункт из меню.")

