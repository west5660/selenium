
# def bank(a,years):
#     per = 0.1
#     for i in range(years):
#         a+=a*0.1
#     return int(a)
# print(bank(500,10),'рублей')
#
#
# spisok = [31,28,31,30,31,30,31,31,30,31,30,31]
# def data(d,m,y):
#     if isinstance(y,int) and isinstance(m,int) and isinstance(d,int):
#         if m>0 and m<13:
#             if d>0 and d<32:
#                 if d>0 and d<=spisok[m-1]:
#                     return True
#
#     return False
# print(data(12,10,2000))
# print(data(12,13,2000))
#
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# def f3(letters):
#     newl=''
#     for l in letters:
#         if l.isupper():
#             continue
#         else:
#             newl +=l
#     return newl
# print(f3(letters))
#selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()                                          #открываем браузер
driver.get('https://www.google.com')                               #заходим на сайт
elem1 = driver.find_element(By.ID,"APjFqb")                        #место ввода для поиска
print(elem1)

# elem1.submit()
elem2 = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")      #нашли кнопку поиск
elem1.send_keys('крутые бобры')                                     #пишем текст поиска
elem2.click()                                                       #клик по кнопке


time.sleep(3)
driver.close()