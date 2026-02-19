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
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    driver.execute_script("window.scrollBy(0, -100);")
    driver.execute_script("arguments[0].click();", element)


# Open homepage
driver.get(URL)

# Go to Books
safe_click((By.XPATH, "//h5[text()='Book Store Application']"))
wait.until(EC.url_contains("/books"))
print("✅ Masuk halaman Books")

# Go to Login page
safe_click((By.ID, "login"))
wait.until(EC.url_contains("/login"))
print("✅ Masuk halaman Login")

# Input credentials
wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("pythonstudent")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("PythonStudent123$")

# Click Login button (safe)
safe_click((By.ID, "login"))

print("✅ Tombol login berhasil diklik")

input("Press Enter to close the browser...")
driver.quit()