from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# INPUT VIDEO URL

video_url = input('Enter a YouTube video for SaveSubs: ')

# PRESETS

mime_types = [
    'text/plain', 
    'application/vnd.ms-excel', 
    'text/csv', 
    'application/csv', 
    'text/comma-separated-values', 
    'application/download', 
    'application/octet-stream', 
    'binary/octet-stream', 
    'application/binary', 
    'application/x-unknown'
]
download_dir = r'C:\Users\Lucas\Documents\python\youtube_ads_project\subs'
savesubs_url = 'https://savesubs.com'

# FIREFOX DOWNLOAD PREFERENCES

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # 0 FOR DESKTOP, 1 FOR DEFAULT DOWNLOAD FOLDER, 2 FOR CUSTOM
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', download_dir) # CUSTOM DOWNLOAD FOLDER
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ",".join(mime_types))

# DEFINING CAPTIONS DOWNLOAD FUNCTION

def captions_download():

    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get(savesubs_url)
    url_input = driver.find_element_by_name('url')
    url_input.send_keys(video_url)
    driver.find_element_by_xpath('/html/body/section/div/div/section[1]/div[2]/input').click()
    # WAIT FOR DOWNLOAD "BUTTON"
    driver_wait = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/main/section[1]/div[1]/ul/li[1]/a'))
    )
    # CLICK DOWNLOAD "BUTTON"
    driver.find_element_by_xpath('/html/body/section/div/div/main/section[1]/div[1]/ul/li[1]/a').click()

captions_download()        
