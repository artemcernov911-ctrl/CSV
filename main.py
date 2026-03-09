import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

browser = webdriver.Chrome()
urls = "https://www.divan.ru/nizhny-novgorod/category/skafy-i-stellazi"
browser.get(urls)
time.sleep(3)


mebel = browser.find_elements(By.CSS_SELECTOR, 'div.CatalogContent_item__Zinr3')
novaitabl = []

for item in mebel:
    try:
        name_element = item.find_element(By.CSS_SELECTOR, "div[itemprop='name']")
        name = name_element.get_attribute("innerHTML")
        price_element = item.find_element(By.CSS_SELECTOR, "meta[itemprop='price']")
        price = price_element.get_attribute('content') + " руб."
        link_element = item.find_element(By.CSS_SELECTOR, "a[href*='/product/']")
        url = link_element.get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    novaitabl.append([name, price, url])

browser.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'Ссылка'])
    writer.writerows(novaitabl)

