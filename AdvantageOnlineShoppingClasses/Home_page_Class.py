from selenium import webdriver
from selenium.webdriver.common.by import By


class Home_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers_category(self):
        return self.driver.find_element(By.ID, "speakersImg")

    def tablets_category(self):
        return self.driver.find_element(By.ID, "tabletsImg")

    def headphones_category(self):
        return self.driver.find_element(By.ID, "headphonesImg")

    def laptops_category(self):
        return self.driver.find_element(By.ID, "laptopsImg")

    def mice_category(self):
        return self.driver.find_element(By.ID, "miceImg")


    def click_speakers(self):
        self.speakers_category().click()

    def click_tablets(self):
        self.tablets_category().click()

    def click_headphones(self):
        self.headphones_category().click()

    def laptops_headphones(self):
        self.laptops_category().click()

    def mice_headphones(self):
        self.mice_category().click()

   



