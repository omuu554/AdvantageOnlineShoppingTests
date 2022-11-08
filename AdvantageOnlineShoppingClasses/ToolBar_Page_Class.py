from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class ToolBarClass:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def Get_AdvLogo_Element(self):
        "returns the element of the SiteLogo in the toolbar"
        return self.driver.find_element(By.CSS_SELECTOR,"a[ng-click='go_up()']")

    def Get_MenuSearchIcon_Element(self):
        "returns the element of the SearchIcon in the toolbar"
        return self.driver.find_element(By.ID, "menuSearch")

    def Get_Usericon_Element(self):
        "returns the element of the UserIcon in the toolbar"
        return self.driver.find_element(By.ID,"menuUserLink")

    def Get_Carticon_Element(self):
        "returns the element of the CartIcon in the toolbar"
        return self.driver.find_element(By.ID,"menuCart")

    def Get_CloseSearch_Element(self):
        "returns the element of the X in the searchBar after it has been opened in the toolbar"
        if(self.driver.find_element(By.ID,"autoComplete").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR,"div[data-ng-click='closeSearchForce()']")
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR,"div[data-ng-click='closeSearchForce()']")

    def Get_SearchBar_Element(self):
        "returns the element of the Searchbar after it has been opened in the toolbar"
        if (self.driver.find_element(By.ID, "autoComplete").is_displayed()):
            return self.driver.find_element(By.ID,"autoComplete")
        self.Get_MenuSearchIcon_Element().click()
        return self.driver.find_element(By.ID,"autoComplete")

    def Click_SearchBar(self):
        "Presses Enter after the searchbar Has been Opened in the toolbar"
        SearchIconElement = self.Get_SearchBar_Element()
        SearchIconElement.send_keys(Keys.ENTER)


    def Get_ItemsAmountInCart_Element(self):
        "returns the element of the Amount of items cartIcon in the toolbar"
        return self.driver.find_element(By.XPATH, "//tfoot/tr[1]/td/span/label")

    def Get_ItemsAmountInCartSTR(self):
        "returns Amount of items in cartIcon, in string form: (x Items)  "
        return self.Get_ItemsAmountInCart_Element().get_attribute("textContent")

    def Get_CartIconCheckOut_Element(self):
        "returns the element of CheckOut button in the cartIcon in toolbar"
        return self.driver.find_element(By.ID,"checkOutPopUp")

    def Get_CartIconItemInfo_Element(self,index:int):
        "returns the element of a spacifice item information from CartIcon in toolbar"
        return self.driver.find_element(By.XPATH,f"//tool-tip-cart/div/table/tbody/tr[{index}]/td[2]/a")

    def Get_CartIconItemName_Element(self,index:int):
        "returns the element of part of the name of a spacifice item from CartIcon in toolbar in format: xxxxxx..."
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH,"//h3")

    def Get_CartIconQuntity_Element(self,index:int):
        "returns the element of the item Quantity of spacifice item in CartIcon in toolbar in form: QTY: x"
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH, "//a/label[1]")

    def Get_CartIconColor_Element(self,index:int):
        "returns the element of the item color of spacifice item in CartIcon in toolbar in form: all upper case letters"
        return self.Get_CartIconItemInfo_Element(index).find_element(By.XPATH, "//label[2]/span")

    def Get_UserIconUsername_Element(self):
        "returns the element of the username after the UserIcon popup is Displayed"
        if(self.driver.find_element(By.CLASS_NAME,"PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "username")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"username")

    def Get_UserIconPassowrd_Element(self):
        "returns the element of the password after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "password")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"password")

    def Get_UserIconRemCheckBox_Element(self):
        "returns the element of the Remember me checkbox after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.NAME, "remember_me")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.NAME,"remember_me")

    def Get_UserIconSignIn_Element(self):
        "returns the element of the SignIn button after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.ID, "sign_in_btnundefined")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.ID,"sign_in_btnundefined")

    def Get_UserIconCreateAccount_Element(self):
        "returns the element of the Create New Account button after the UserIcon popup is Displayed"
        if (self.driver.find_element(By.CLASS_NAME, "PopUp").is_displayed()):
            return self.driver.find_element(By.CLASS_NAME, "create-new-account")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.CLASS_NAME, "create-new-account")

    def Get_UserIconSignOut_Element(self):
        "returns the element of the SignOut button after UserIcon was Pressed(User Must be Signed In for it to work)"
        if(self.driver.find_element(By.CSS_SELECTOR,"label[translate='Sign_out'][role='link']").is_displayed()):
            return self.driver.find_element(By.CSS_SELECTOR,"label[translate='Sign_out'][role='link']")
        self.Get_Usericon_Element().click()
        return self.driver.find_element(By.CSS_SELECTOR, "label[translate='Sign_out'][role='link']")

    def IsUserSignedIn(self,username:str):
        "returns true if the user is signed in"
        return self.driver.find_element(By.CSS_SELECTOR,"#menuUserLink>span").text == username

    def Wait_UserSignIn(self,username:str):
        "Wait for user to be signed in"
        while(not self.IsUserSignedIn(username)):
            pass








