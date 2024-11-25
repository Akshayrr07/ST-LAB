from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Correct path to ChromeDriver
chrome_driver_path = r"D:\PROJECTS\ST\ST-LAB\chromedriver.exe"

# Initialize the ChromeDriver using Service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("http://selenium.dev")


