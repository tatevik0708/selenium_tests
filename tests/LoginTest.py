from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #executable_path='C:/webdrivers/chromedriver'

driver.get('http://the-internet.herokuapp.com/login')

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
loginbutton = driver.find_element(By.CSS_SELECTOR, '#login > button > i')

username.click()
username.send_keys('tatevik')
password.click()
password.send_keys('tttttt')
loginbutton.click()
driver.quit()



