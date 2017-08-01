from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from linkedin.items import LinkedinItem
import pickle, os
import unittest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from lxml import html

# def getCookie():
#     driver = webdriver.Chrome()
#     driver.get("https://www.linkedin.com")
#     driver.find_element(By.ID, "login-email").send_keys("shrivastava.shubham219@live.com")
#     driver.find_element(By.ID, "login-password").send_keys("Shubham@25")
#     driver.find_element(By.CSS_SELECTOR, "[type='submit'][value='Sign in']").click()
#     driver.maximize_window()
#     listcookies = driver.get_cookies()
#     return listcookies

def striplist(l):
    l = [x.strip().replace('\t',"") for x in l]
    return [x for x in l if x != u'']


iterator = 1

class linkedInSpider(Spider):
    name = "linkedin.com"
    details = open("title.txt", "w", encoding=("utf8"))
    details_set = set()

    def __init__(self, *args, **kwargs):
        super(linkedInSpider, self).__init__(*args, **kwargs)
        self.download_delay = 0.25
        #self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(60)        

    def start_requests(self):
        #Passing url from file which is already processed. 
        start_urls = []
        w = open("user_data.txt", 'r')
        for line in w:
            start_urls.append(line)

        #Uncomment this to pass urls manually. 
        #start_urls = ["https://www.linkedin.com/in/shubhamshrivastav/","https://www.linkedin.com/in/ashwani-kumar-97465186/"]
        self.browser.get("https://www.linkedin.com")
        #driver.get("https://www.linkedin.com")
        userid = input("User Id? ")
        passwd = input("Pasword? ")
        self.browser.find_element(By.ID, "login-email").send_keys(userid)
        self.browser.find_element(By.ID, "login-password").send_keys(passwd)
        self.browser.find_element(By.CSS_SELECTOR, "[type='submit'][value='Sign in']").click()
        for url in start_urls:
            yield Request(url=url, cookies=self.browser.get_cookies(), callback=self.parse)
    

    def parse(self, response):
        #self.log('-----------------------------------------------------')
        self.browser.get(response.url)
        time.sleep(5)

        #Click on show more link to retrieve user's details containing email, url etc
        self.browser.find_element_by_css_selector('.contact-see-more-less.link-without-visited-state').click()
        time.sleep(4)
        js = '''var email = document.querySelectorAll('span.pv-contact-info__contact-link');
                return email[0].innerHTML;'''
        try:
            js2 = ''' var name = $('span.pv-contact-info__contact-link').parent().parent().prop('className');
                     return name;
             '''
            parentname = self.browser.execute_script(js2)
            if "ci-email" in parentname:
                email = self.browser.execute_script(js)
            else:
                email = "Not Available"
        except Exception as e:
            email = "Not Available"
        source = self.browser.page_source
        soup = BeautifulSoup(source, 'html.parser')
        title = soup.find('h2', class_='pv-top-card-section__headline')
        name = soup.find("h1", class_="pv-top-card-section__name")

        item = LinkedinItem()
        item['name'] = name.string
        item['url'] = response.url
        item['title'] = title.string
        item['email'] = email.strip()
        # hxs = HtmlXPathSelector(response)
        # item = LinkedinItem()
        # item['url'] = response.url
        # item['title'] = striplist(hxs.select('//a/@href').extract())
        # HTMLtitle = striplist(hxs.select('//title/text()').extract())
        # item['name'] = [HTMLtitle[0].split('|')[0].strip()]
        # item['summary'] = striplist(hxs.select('//section/div[@class="description"]/p/text()').extract())
        # ref = response.request.headers.get('Referer', None)
        yield item