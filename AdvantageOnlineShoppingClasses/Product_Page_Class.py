from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class ProductClass:

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def Get_ProductName_Element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h1")

    def Get_ProudctPrice_Element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h2")