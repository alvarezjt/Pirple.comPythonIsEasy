#import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class Five9App():
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def Open(self):
        self.MyPATH = os.getcwd() + '\\chromedriver.exe'
        self.MyDriver = webdriver.Chrome(self.MyPATH)
        self.MyDriver.get("https://app.five9.com/index.html")
        time.sleep(5)

        #Fill in the login form.
        self.MyDriver.find_element_by_id("Login-username-input").send_keys(self.Username) #Send username to form
        time.sleep(1)
        self.MyDriver.find_element_by_id("Login-password-input").send_keys(self.Password) #Send password to form
        time.sleep(1)
        self.MyDriver.find_element_by_id("Login-login-button").click() #Invoke click action on login button

    def WaitForElement(self,ByCriteria,Element,Action="None"):
        self.Action = Action
        try:
            if (ByCriteria == "ID"):
                ElementCheck = WebDriverWait(Five9App.MyDriver,30).until(
                    EC.presence_of_element_located((By.ID,Element))
                )
            elif (ByCriteria == "ClassName"):
                ElementCheck = WebDriverWait(Five9App.MyDriver,30).until(
                    EC.presence_of_element_located((By.CLASS_NAME,Element))
                )
            elif (ByCriteria == "XPath"):
                ElementCheck = WebDriverWait(Five9App.MyDriver,30).until(
                    EC.presence_of_element_located((By.XPATH,Element))                
                )
            if (self.Action == "Click"):
                ElementCheck.click()
            return True
        except:
            return False

    def Close(self):
        #MyDriver.close() #Close the browser tab #MyDriver.quit() #Close the browser
        self.MyDriver.quit()

Five9App = Five9App(input("Username: "),input("Password: "))
Five9App.Open()
time.sleep(5)
Five9App.WaitForElement("ID","OkCancelDialog-force-button","Click")
time.sleep(10)
Five9App.WaitForElement("ClassName","supervisor","Click")
time.sleep(10)
Five9App.WaitForElement("XPath",'//*[@id="StationTypeSwitch"]/div/label[4]',"Click")
time.sleep(5)
Five9App.WaitForElement("ClassName","pull-right","Click")
print("Clicking the Agents tab in 5 seconds.")
time.sleep(5)
Five9App.WaitForElement("XPath",'//*[@id="SuperContent"]/div/div[1]/div[1]/ul/li[2]/a',"Click")
print("Agents tab clicked, closing the browser in 20 seconds.")
time.sleep(20)
Five9App.Close()