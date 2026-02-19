import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from config import *

# ==============================
# SETUP CHROME OPTIONS
# ==============================
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)

# ==============================
# CREATE DRIVER
# ==============================
service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 15)


# ==============================
# SAFE CLICK FUNCTION
# ==============================
def safe_click(locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("window.scrollBy(0, -100);")
    driver.execute_script("arguments[0].click();", element)


# ==============================
# 1️⃣ OPEN HOMEPAGE
# ==============================
driver.get(URL)

# ==============================
# 2️⃣ BOOK STORE APPLICATION
# ==============================
safe_click((By.XPATH, "//h5[text()='Book Store Application']"))
wait.until(EC.url_contains("/books"))
print("✅ Masuk halaman Books")

# ==============================
# 3️⃣ LOGIN PAGE
# ==============================
safe_click((By.ID, "login"))
wait.until(EC.url_contains("/login"))
print("✅ Masuk halaman Login")

# ==============================
# 4️⃣ LOGIN
# ==============================
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("pythonstudent")
driver.find_element(By.ID, "password").send_keys("PythonStudent123$")

safe_click((By.ID, "login"))
wait.until(EC.url_contains("/profile"))
print("✅ Login berhasil, masuk Profile")

# ==============================
# 5️⃣ KEMBALI KE HOMEPAGE
# ==============================
driver.get("https://demoqa.com")

# ==============================
# 6️⃣ CLICK ELEMENTS
# ==============================
safe_click((By.XPATH, "//h5[text()='Elements']"))
wait.until(EC.url_contains("/elements"))
print("✅ Klik menu Elements berhasil")

# ==============================
# 7️⃣ CLICK TEXT BOX
# ==============================
safe_click((By.XPATH, "//span[text()='Text Box']"))
wait.until(EC.url_contains("/text-box"))
print("✅ Klik menu Text Box berhasil")

# ==============================
# 8️⃣ ISI FORM
# ==============================
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("John Doe")
driver.find_element(By.ID, "userEmail").send_keys("john@doe.com")
driver.find_element(By.ID, "currentAddress").send_keys("Alamat sekarang")
driver.find_element(By.ID, "permanentAddress").send_keys("Alamat tetap")

safe_click((By.ID, "submit"))
print("✅ Form berhasil disubmit")

# ==============================
# 9️⃣ CLICK UPLOAD AND DOWNLOAD
# ==============================
safe_click((By.XPATH, "//span[text()='Upload and Download']"))
wait.until(EC.url_contains("/upload-download"))
print("✅ Masuk halaman Upload and Download")

# ==============================
# 🔟 DOWNLOAD FILE
# ==============================
safe_click((By.ID, "downloadButton"))
print("✅ File berhasil didownload ke:", download_path)

input("Press Enter to close the browser...")
driver.quit()