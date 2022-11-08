from selenium import webdriver
from selenium.webdriver.common.by import By


class Category_Page_Advantage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product(self, id: int):
        return self.driver.find_element(By.ID, f"{id}")
    def product_name(self, id: int):
        return self.driver.find_element(By.XPATH, f"//img[@id='{id}']/../p[1]/a")

    def product_price(self, id: int):
        return self.driver.find_element(By.XPATH, f"//img[@id='{id}']/../p[2]/a")

    def click_product(self, id: int):
        self.product(id).click()

