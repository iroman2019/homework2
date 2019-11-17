from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def filter(word):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.NAME, "query").send_keys(word)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

filter("John")

def delete_emp(id):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    #result = driver.find_element(By.XPATH, "//tr[td[text()='" + id + "']]/td[last()]")
    driver.find_element(By.XPATH, "//tr[td[a[text()='"+id+"']]]/td[last()]/form/input[2]").click()



