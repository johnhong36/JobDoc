from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
import time

def scrapeData(website:str):
    source = requests.get(website).content
    soup = BeautifulSoup(source,"lxml")
    print(soup.prettify())


    return soup

    #Indeed, Linkedn, Monster, Ziprecruiter

def scrapeIndeed(website:str):
    DRIVER_PATH = "/home/jhong/chromedriver/chromedriver_linux64/chromedriver"

    options = Options()
    options.headless = True


    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(website)

    nameXPath = "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    print(nameElem.text)


    descXPath = "//div[@class='jobsearch-jobDescriptionText']"
    descElem = driver.find_element_by_xpath(descXPath)
    print(descElem.text)


    driver.quit()


    #Indeed, Linkedn, Monster, Ziprecruiter


if __name__ == "__main__":
    scrapeIndeed("https://www.indeed.com/q-Software-Engineer-jobs.html?advn=5014086920423836&vjk=b2dda17b12a5ed79")


