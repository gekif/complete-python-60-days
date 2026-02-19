from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

wait = WebDriverWait(driver, 15)


def safe_click(locator):
    element = wait.until(EC.element_to_be_clickable(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("window.scrollBy(0, -100);")
    driver.execute_script("arguments[0].click();", element)


# 1️⃣ Open homepage
driver.get(URL)

# 2️⃣ Book Store
safe_click((By.XPATH, "//h5[text()='Book Store Application']"))
wait.until(EC.url_contains("/books"))
print("✅ Masuk halaman Books")

# 3️⃣ Login
safe_click((By.ID, "login"))
wait.until(EC.url_contains("/login"))
print("✅ Masuk halaman Login")

# 4️⃣ Fill Login
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("pythonstudent")
driver.find_element(By.ID, "password").send_keys("PythonStudent123$")

safe_click((By.ID, "login"))
wait.until(EC.url_contains("/profile"))
print("✅ Login berhasil, masuk Profile")

# 5️⃣ Kembali ke homepage
driver.get("https://demoqa.com")

# 6️⃣ Click Elements
safe_click((By.XPATH, "//h5[text()='Elements']"))
wait.until(EC.url_contains("/elements"))
print("✅ Klik menu Elements berhasil")

# 7️⃣ Click Text Box (FIXED)
safe_click((By.XPATH, "//span[text()='Text Box']"))
wait.until(EC.url_contains("/text-box"))
print("✅ Klik menu Text Box berhasil")

# 8️⃣ Isi Form
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("John Doe")
driver.find_element(By.ID, "userEmail").send_keys("john@doe.com")
driver.find_element(By.ID, "currentAddress").send_keys("Alamat sekarang")
driver.find_element(By.ID, "permanentAddress").send_keys("Alamat tetap")

safe_click((By.ID, "submit"))
print("✅ Form berhasil disubmit")

input("Press Enter to close the browser...")
driver.quit()