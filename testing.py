from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver
chromedriver_path = r"D:\PROJECTS\ST\ST-LAB\chromedriver.exe"  # Update this path

# Path to the Chromium browser executable
chromium_binary_path = r"D:\SOFTWARES\chrome-win\chrome.exe"  # Update this path

# Set up ChromeDriver for Chromium
service = Service(chromedriver_path)
options = webdriver.ChromeOptions()
options.binary_location = chromium_binary_path

# Initialize the WebDriver for Chromium
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Amazon
    driver.get("https://www.amazon.in")
    print("Amazon homepage opened.")

    # Maximize the browser window
    driver.maximize_window()

    # Wait for the search bar to be present
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

    # Search for a product (e.g., "laptop")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    print("Search initiated for 'laptop'.")

    # Wait for the search results to load and click on the first product
    first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item")))
    first_product.find_element(By.CSS_SELECTOR, "h2 a").click()
    print("First product selected.")

    # Switch to the new tab (Amazon opens products in a new tab)
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the "Add to Cart" button to be present and click it
    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    print("Product added to cart.")

    # Wait for confirmation message (optional)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-size-medium.a-color-base.sc-product-title")))
    print("Product successfully added to cart.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
    print("Test completed and browser closed.")
