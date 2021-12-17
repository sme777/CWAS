from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import argparse

def activate_selenium_driver(windows, download_path, input_path):
    
    for i in range(windows):
        # set up firefox profile
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        
        if download_path != "":
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.download.dir', download_path)
        
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-gzip, application/x-tar')
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        
        # set up webdriver
        driver = webdriver.Firefox(profile)
        driver.implicitly_wait(15)
        driver.get("https://hb.flatironinstitute.org/deepsea/")
        driver.find_element_by_id("formDeepSEAFile").send_keys(input_path +"/fasta"+ str(i) +".fasta")
        driver.find_element_by_class_name("btn-primary").click()
        try:
            element = WebDriverWait(driver, 30).until(
                 EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/table[1]/tbody/tr[6]/td[2]/a"))
            )
            element.click()
        finally:
            driver.quit()

parser = argparse.ArgumentParser()
parser.add_argument('--windows', type=int, help='Optional Number of Files to Run Selenium')
parser.add_argument('--path', type=str, help="Optional Custom Download Path")
parser.add_argument('--folder', type=str, help="Folder to Upload Fasta Files from")
args = parser.parse_args()
windows = args.windows or 100
download_path = args.path or ""
input_path = args.folder or "~/Desktop/cs194/lung_fasta/fasta"

activate_selenium_driver(windows, download_path, input_path)

