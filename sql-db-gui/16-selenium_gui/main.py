import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from config import *


# ==============================
# BASE PAGE (Reusable Methods)
# ==============================
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def safe_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("window.scrollBy(0, -100);")
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_url_contains(self, text):
        self.wait.until(EC.url_contains(text))


# ==============================
# MAIN APPLICATION CLASS
# ==============================
class DemoQAApp(BasePage):

    def open_homepage(self):
        self.driver.get(URL)

    def go_to_bookstore(self):
        self.safe_click((By.XPATH, "//h5[text()='Book Store Application']"))
        self.wait_url_contains("/books")
        print("✅ Masuk halaman Books")

    def go_to_login(self):
        self.safe_click((By.ID, "login"))
        self.wait_url_contains("/login")
        print("✅ Masuk halaman Login")

    def login(self, username, password):
        self.type_text((By.ID, "userName"), username)
        self.type_text((By.ID, "password"), password)
        self.safe_click((By.ID, "login"))
        self.wait_url_contains("/profile")
        print("✅ Login berhasil, masuk Profile")

    def go_to_elements(self):
        self.driver.get("https://demoqa.com")
        self.safe_click((By.XPATH, "//h5[text()='Elements']"))
        self.wait_url_contains("/elements")
        print("✅ Klik menu Elements berhasil")

    def fill_text_box(self):
        self.safe_click((By.XPATH, "//span[text()='Text Box']"))
        self.wait_url_contains("/text-box")
        print("✅ Klik menu Text Box berhasil")

        self.type_text((By.ID, "userName"), "John Doe")
        self.type_text((By.ID, "userEmail"), "john@doe.com")
        self.type_text((By.ID, "currentAddress"), "Alamat sekarang")
        self.type_text((By.ID, "permanentAddress"), "Alamat tetap")

        self.safe_click((By.ID, "submit"))
        print("✅ Form berhasil disubmit")

    def download_file(self):
        self.safe_click((By.XPATH, "//span[text()='Upload and Download']"))
        self.wait_url_contains("/upload-download")
        print("✅ Masuk halaman Upload and Download")

        self.safe_click((By.ID, "downloadButton"))
        print("✅ File berhasil didownload")


# ==============================
# DRIVER SETUP
# ==============================
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")

    download_path = os.getcwd()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(executable_path=CHROME_DRIVER)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    return driver


# ==============================
# MAIN EXECUTION
# ==============================
if __name__ == "__main__":

    driver = create_driver()
    app = DemoQAApp(driver)

    app.open_homepage()
    app.go_to_bookstore()
    app.go_to_login()
    app.login("pythonstudent", "PythonStudent123$")
    app.go_to_elements()
    app.fill_text_box()
    app.download_file()

    input("Press Enter to close the browser...")
    driver.quit()
