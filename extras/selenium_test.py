from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('C:\Windows\chromedriver\chromedriver.exe')
driver.get('https://www.artofvisualization.com')
sleep(1)

driver.get_screenshot_as_file("screenshot_selenium.png")
driver.quit()
print('screen shot is complete')
