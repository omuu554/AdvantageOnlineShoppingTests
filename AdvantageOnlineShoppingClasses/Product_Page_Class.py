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

    def ProductPriceDigits(self):
        return re.sub(r'[^0-9.]', '', self.Get_ProudctPrice_Element().text)

    def Get_ProudctDescription_Element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>p")

    def Get_ProductColor_Element(self,Color:str):
        return self.driver.find_element(By.CSS_SELECTOR, f"span[title='{Color.upper()}']")

    def Get_ProductQuantityMinus_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "minus")

    def Get_ProductQuantityMinus_Element(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

