from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def multiplyWithForm(a, b):
    driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")
    driver.find_element(By.ID, "a-input").send_keys(a)
    driver.find_element(By.ID, "b-input").send_keys(b)
    driver.find_element(By.ID, "calculate-button").click()
    result = int(driver.find_element(By.ID, "result-div").text)
    return result

def multiplyWithTable(a, b):
    driver.get("http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html")
    result = int(driver.find_element(By.XPATH, "//tr["+str(a)+"]/td["+str(b)+"]").text)
    return result

def multiply(a, b):
    return a * b

first_number = int(input("The first number: "))
second_number = int(input("The second number: "))
#print(type(second_number))
first_multiplication = multiplyWithForm(first_number, second_number)
second_multiplication = multiplyWithTable(first_number, second_number)
third_multiplication = multiply(first_number, second_number)
print("The first multiplication: " + str(first_multiplication))
print("The second multiplication: " + str(second_multiplication))
print("The third multiplication: " + str(third_multiplication))
print(first_multiplication == second_multiplication)
print(second_multiplication == third_multiplication)


