from selenium import webdriver
#one we give the login credentials, we click "enter key" and hence importing key is required
from selenium.webdriver.common.keys import Keys
import time

def get_driver():

  #set options to make the browsing easier
  options = webdriver.ChromeOptions()
  #to disable the info bars so that they wont interrupt script processing
  options.add_argument("disable-infobars")
  
  # to start the browser maximized
  options.add_argument("start-maximized")
  
  # to disable certain parameters on linux machine
  options.add_argument("disable-dev-shm-usage")
  
  # to have more previlages and sandboxes are disabled
  options.add_argument("no-sandbox")
  
  # to exclude switches and enable automation
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  
  # to exclude blink features
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

#to get only the dynamic value and remove the text associated with it
def clean_text(text):
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  
  #find element by xpath is not supported and hence here find element has been 
  #used with "by" and "value" arguments.
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  #to click on "HOME" button after login, when we inspected it we found that it is of type xpath
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(5)

  #to scrape the dynamic value after login
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

  return clean_text(element.text)
  #to print the url name in the console
  print(driver.current_url)

print(main())

