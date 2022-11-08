from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class ToolBarClass:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def Get_AdvLogo_Element(self):
        return self.driver.find_element(By.CSS_SELECTOR,"a[ng-click='go_up()']")

    def Get_MenuSearchIcon_Element(self):
        return self.driver.find_element(By.ID, "menuSearch")

    def Get_Usericon_Element(self):
        return self.driver.find_element(By.ID,"menuUserLink")

    def Get_Carticon_Element(self):
        return self.driver.find_element(By.ID,"menuCart")

    def Get_CloseSearch_Element(self):
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR,"div[data-ng-click='closeSearchForce()']")

    def Get_SearchBar_Element(self):
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.ID,"autoComplete")

    def Click_SearchBar(self):
        SearchIconElement = self.Get_SearchBar_Element()
        SearchIconElement.send_keys(Keys.ENTER)


    def Get_ItemsAmountInCart_Element(self):
        return self.driver.find_element(By.XPATH, "//tfoot/tr[1]/td/span/label")

    def Get_ItemsAmountInCartSTR(self):
        return self.Get_ItemsAmountInCart_Element().get_attribute("textContent")

    def Get_CartIconCheckOut_Element(self):
        return self.driver.find_element(By.ID,"checkOutPopUp")

    def Get_CartIconItemInfo_Element(self,index:int):
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a")

    def Get_CartIconItemName_Element(self,index:int):
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH,"//h3")

    def Get_CartIconQuntity_Element(self,index:int):
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH, "//a/label[1]")

    def Get_CartIconColor_Element(self,index:int):
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH, "//label[2]/span")





