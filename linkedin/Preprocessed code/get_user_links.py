import unittest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from lxml import html

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")
uid = input("UserId")
pswd = input("Pswd")
driver.find_element(By.ID, "login-email").send_keys(uid)
driver.find_element(By.ID, "login-password").send_keys(pswd)
driver.find_element(By.CSS_SELECTOR, "[type='submit'][value='Sign in']").click()
driver.maximize_window()

listcookies = driver.get_cookies()


headers = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
url = "https://www.linkedin.com/search/results/people/?keywords=meditation&origin=GLOBAL_SEARCH_HEADER&page="
i = 0
w = open("user_data.txt", "w", encoding="utf8")

myset = set()
while True:
    i = i+1
    driver.get(url + str(i))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    all_anchor = soup.find_all('a', class_='search-result__result-link ember-view')
    if len(all_anchor)==0:
        break
    print(len(all_anchor))
    for anchor in all_anchor:
        link = anchor.get("href")
        link = "https://www.linkedin.com" + link
        myset.add(link)
        print(link)
print(myset)
for element in myset:
    w.write(element + "\n")
w.close()