from selenium import webdriver
import time #ejecutar una prueba y que se pueda ver el proceso

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

#driver.maximize_window() #nos permite maximixar el browser

driver.get("https://google.com") #setear la URl

driver.find_element_by_id("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
buscar = driver.find_element_by_id("html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
buscar.send_keys("Leonardo")



time.sleep(2)


driver.quit()