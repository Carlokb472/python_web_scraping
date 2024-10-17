import os
import time
import wget
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up the Chrome WebDriver using WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Locate the search box, enter "cats" and hit Enter
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)
search_box.send_keys("cats")
search_box.send_keys(Keys.RETURN)

# Click on the 'Images' tab to search for images
images_tab = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "圖片"))
)
images_tab.click()

# Wait for the images to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "img"))
)

# Scroll down to load more images
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find all image elements
image_elements = driver.find_elements(By.TAG_NAME, "img")

# Download the first 30 images
download_folder = "cats_images"
if not os.path.exists(download_folder):
    os.mkdir(download_folder)

count = 0
for img in image_elements:
    if count >= 30:
        break
    img_url = img.get_attribute("src")
    if img_url and img_url.startswith("http"):
        try:
            save_as = os.path.join(download_folder, f"cat_{count}.jpg")
            wget.download(img_url, save_as)
            print(f"Downloaded: {save_as}")
            count += 1
        except Exception as e:
            print(f"Failed to download image {count}: {e}")

# Close the browser
driver.quit()

print(f"Downloaded {count} images.")
