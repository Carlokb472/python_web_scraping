import os
import time

import wget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Use ChromeDriverManager to install the ChromeDriver
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open a website (for example, Instagram)
driver.get("https://www.instagram.com/")

# input("Press Enter to close the browser...")

username = WebDriverWait(driver,10).until(
EC.presence_of_element_located((By.NAME,"username"))
)



password= WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.NAME,"password"))
)


login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
username.clear()
password.clear()
#type your username and the password here
username.send_keys("")
password.send_keys("")

login.click()


clickSearch= WebDriverWait(driver,20).until(
   EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_kC"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div'))
)
clickSearch = driver.find_element(By.XPATH,'//*[@id="mount_0_0_kC"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div')
clickSearch.send_keys(KEY.RETURN)
search= WebDriverWait(driver,20).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_T9"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
)
keyword = "#cat"
search.send_keys(keyword)
time.sleep(1)
search.send_keys(KEY.RETURN)
time.sleep(1)
search.send_keys(KEY.RETURN)



catSearch = driver.find_element(By.XPATH, '//*[@id="mount_0_0_w8"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div')
catSearch.click()



# Wait for images to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_aagw"))
)

# Find all images with the class "_aagw"
imgs = driver.find_elements(By.CLASS_NAME, "_aagw")

path = os.path.join(keyword.strip('#'))  # Remove the hash sign for folder name
if not os.path.exists(path):
    os.mkdir(path)

count = 0
for img in imgs:
    save_as = os.path.join(path,keyword +str(count) +'.jpg')
    wget.download(img.get_attribute("src"),save_as)
    count += 1








#Close the browser
driver.quit()