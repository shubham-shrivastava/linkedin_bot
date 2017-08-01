import unittest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")
driver.find_element(By.ID, "login-email").send_keys("shrivastava.shubham219@live.com")
driver.find_element(By.ID, "login-password").send_keys("Shubham@25")
driver.find_element(By.CSS_SELECTOR, "[type='submit'][value='Sign in']").click()
driver.maximize_window()
names = []
groups = open("groups.txt", "w",encoding="utf8")
i = 0
while True:
    i = i+1
    driver.get("https://www.linkedin.com/search/results/groups/?keywords=meditation&origin=GLOBAL_SEARCH_HEADER&page=%s"% str(i))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    all_title = soup.find_all('h3', class_='search-result__title')
    if len(all_title)==0:
        break
    print(len(all_title))
    for title in all_title:
        strng = title.string
        strng = strng + "\n"
        groups.write(strng)
        names.append(strng)
        print(strng)
groups.close()