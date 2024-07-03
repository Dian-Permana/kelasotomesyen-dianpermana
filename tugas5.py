from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)

driver.maximize_window()

driver.get("https://demoqa.com/alerts")

def explicitly_wait(detik):
    try:
        WebDriverWait(driver,detik).until(EC.alert_is_present())
        print("OK alertnya muncul Bang ^_^")

    except TimeoutException:
        print("Gak muncul Bang....!!!")
        pass    

driver.find_element(By.ID,"alertButton").click() #alertButton
explicitly_wait(10)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"timerAlertButton").click() #timerAlertButton
explicitly_wait(10)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"confirmButton").click() #confirmButton dismiss
explicitly_wait(10)
driver.switch_to.alert.dismiss()

driver.find_element(By.ID,"confirmButton").click() #confirmButton accept
explicitly_wait(10)
driver.switch_to.alert.accept()

driver.find_element(By.ID,"promtButton").click() #promtButton
explicitly_wait(10)
driver.switch_to.alert.send_keys("Test 1..2..3..") #promtButton send_keys
driver.switch_to.alert.dismiss()

driver.find_element(By.ID,"promtButton").click() #promtButton
explicitly_wait(10)
driver.switch_to.alert.send_keys("Eusian naon ieu nya") #promtButton send_keys
driver.switch_to.alert.accept()

#driver.close()  #Jika program diaktifkan maka setelah program selesai windows akan tertutup (close)