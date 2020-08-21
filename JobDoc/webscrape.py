from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests


DRIVER_PATH = "/home/jhong/chromedriver/chromedriver_linux64/chromedriver"
options = Options()
options.headless = True

def scrapeData(website:str):
    source = requests.get(website).content
    soup = BeautifulSoup(source,"lxml")
    print(soup.prettify())


    return soup

    #Indeed, Linkedn, Monster, Ziprecruiter

def scrapeIndeed(website:str):
    
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(website)

    nameXPath = "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    print(nameElem.text)


    descXPath = "//div[@class='jobsearch-jobDescriptionText']"
    descElem = driver.find_element_by_xpath(descXPath)
    print(descElem.text)


    driver.quit()

    #print(driver.page_source)
    #Indeed, Linkedn, Monster, Ziprecruiter


def scrapeZipRecruiter(website:str):
    
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(website)

    nameXPath = "//a[@class='job_details_link']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    print(nameElem.text)

    descXPath = "//div[@class='jobDescriptionSection']"
    descElem = driver.find_element_by_xpath(descXPath)
    print(descElem.text)

    driver.quit()
    
    #print(driver.page_source)


def scrapeLinkedin(website:str):
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get(website)

    buttonXPath = "//button[@class='show-more-less-html__button show-more-less-html__button--more']"
    buttonElem = driver.find_element_by_xpath(buttonXPath)
    buttonElem.click()

    nameXPath = "//a[@class='topcard__org-name-link topcard__flavor--black-link']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    print(nameElem.text)

    descXPath = "//div[@class='description__text description__text--rich']"
    descElem = driver.find_element_by_xpath(descXPath)
    print(descElem.text)

    #print(driver.page_source)

    driver.quit()

if __name__ == "__main__":
    # scrapeIndeed("https://www.indeed.com/q-Software-Engineer-jobs.html?advn=5014086920423836&vjk=b2dda17b12a5ed79")
    #scrapeZipRecruiter("https://www.ziprecruiter.com/jobs/tusimple-87c8fb36/software-engineer-full-stack-autonomous-driving-san-diego-105c41e6?lvk=NZ4BvBk3xufoOwwRvDSqQg.--LgmoJtx5-")
    #scrapeZipRecruiter("https://www.ziprecruiter.com/jobs/voice-7c2d77f3/software-engineer-mobile-android-c49bfae6?lvk=rvH7MzFZpn824Km1Kt395Q.--Lgo40fOCk")
    scrapeLinkedin("https://www.linkedin.com/jobs/view/software-engineer-at-rightclick-1964159937?refId=20378dc5-fd17-4874-a927-c0517efcfe47&trk=public_jobs_topcard_title")


    