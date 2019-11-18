from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def filter(word):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.NAME, "query").send_keys(word)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

#filter("John")

def delete_emp(id):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    #result = driver.find_element(By.XPATH, "//tr[td[text()='" + id + "']]/td[last()]")
    driver.find_element(By.XPATH, "//tr[td[a[text()='"+id+"']]]/td[last()]/form/input[2]").click()

def delete_emp_name(name):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    #print(driver.find_element(By.XPATH, "//tr[td[contains(text(),'"+name+"')]]/td[2]").text)
    #driver.find_element(By.XPATH, "//tr[td[text()='"+name+"']]/td[last()]/form/input[2]").click()

    driver.find_element(By.XPATH, "//tr[td[contains(text(),'"+name+"')]]/td[last()]/form/input[2]").click()

#delete_emp_name("Captain America")

def how_many_employee():
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    print("hello")
    #rowCount = len(driver.find_element(By.XPATH, "//tr"))
    rowCount = driver.execute_script("return document.getElementsByTagName('tr').length")
    print(str(rowCount-1))

how_many_employee()

def to_hungarian():
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.XPATH, "//a[text()='Magyar']").click()

to_hungarian()

def to_english():
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.XPATH, "//a[text()='English']").click()

to_english()

def fill_employee(name):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.XPATH, "//a[text()='Create employee']").click()
    #driver.find_element(By.ID, "create-form:name-input").click()
    driver.find_element(By.ID, "create-form:name-input").send_keys(name)
    driver.find_element(By.ID, "create-form:save-button").click()
    #driver.find_element(By.ID, "create-form:save-button").click()


#fill_employee("Benő")

def error_message():
    return driver.find_element(By.CLASS_NAME, "invalid-feedback").text

fill_employee("")
print(error_message())

def fill_card_number(card_number):
    driver.find_element(By.ID, "create-form:card-number-input").send_keys(str(card_number))
    driver.find_element(By.ID, "create-form:save-button").click()

def fill_full_employee(name, card_number):
    fill_employee(name)
    fill_card_number(card_number)

#fill_full_employee("Hakapeszi Maki", 234)

def modify_emp(old_name, new_name):
    driver.get("http://www.learnwebservices.com/empapp/employees.xhtml")
    driver.find_element(By.XPATH, "//tr[td[contains(text(),'" + old_name + "')]]/td[1]/a").click()
    driver.find_element(By.XPATH, "//input[@value='"+old_name+"']").clear()
    driver.find_element(By.XPATH, "//input[@value='"+old_name+"']").send_keys(new_name)
    driver.find_element(By.XPATH, "//input[@value='Update employee']").click()

#modify_emp("Hakapeszi Maki", "Ha kap eszi Maki")
