from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from JobDoc.database import Company, Skill

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')

def scrapeAll(website:str):
    driver = webdriver.Chrome(options=options)
    driver.get(website)

    a_Text = driver.find_elements_by_tag_name('a')
    for z in a_Text:
        print(z.text)
    
    h1_Text = driver.find_elements_by_tag_name('h1')
    for z in h1_Text:
        print(z.text)

    p_Text = driver.find_elements_by_tag_name('p')
    for x in p_Text:
        print(x.text)

    br_Text = driver.find_elements_by_tag_name('br')
    for y in br_Text:
        print(y.text)

    li_Text = driver.find_elements_by_tag_name('li')
    for z in li_Text:
        print(z.text)

    #print(driver.page_source)

    driver.quit()

    return "None", "None"
    

def scrapeIndeed(website:str):
    driver = webdriver.Chrome(options=options)
    driver.get(website)

    nameXPath = "//div[@class='icl-u-lg-mr--sm icl-u-xs-mr--xs']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    name = nameElem.text

    descXPath = "//div[@class='jobsearch-jobDescriptionText']"
    descElem = driver.find_element_by_xpath(descXPath)
    skills = getSkills(descElem.text)

    driver.quit()

    return name, skills


def scrapeZipRecruiter(website:str):
    driver = webdriver.Chrome(options=options)
    driver.get(website)

    nameXPath = "//span[@class='job_location_item job_location_name']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    name = nameElem.text

    descXPath = "//div[@id='job_desc']"
    descElem = driver.find_element_by_xpath(descXPath)
    skills = getSkills(descElem.text)

    driver.quit()

    return name, skills


def scrapeLinkedin(website:str):
    driver = webdriver.Chrome(options=options)
    driver.get(website)

    buttonXPath = "//button[@class='show-more-less-html__button show-more-less-html__button--more']"
    buttonElem = driver.find_element_by_xpath(buttonXPath)
    buttonElem.click()

    nameXPath = "//a[@class='topcard__org-name-link topcard__flavor--black-link']"
    nameElem = driver.find_element_by_xpath(nameXPath)
    name = nameElem.text

    descXPath = "//div[@class='description__text description__text--rich']"
    descElem = driver.find_element_by_xpath(descXPath)
    skills = getSkills(descElem.text)

    driver.quit()

    return name, skills


def getSkills(descText):
    descList = descText.split(" ")
    skillList = {skill.name for skill in Skill.query.all()}
    jobSkills = []
    lower = []
    returnVal = ""

    for word in descList:
        if word[-1] == ",":
            word = word[:-1]

        if word.lower() in skillList and word.lower() not in lower:
            jobSkills.append(word)
            lower.append(word.lower())

    
    for index in range(len(jobSkills)):
        if index == 4 or index == len(jobSkills)-1:
            returnVal += jobSkills[index]
            break
        else:
            returnVal += jobSkills[index] + ", "

    return returnVal
