from selenium import webdriver

driver = webdriver.Chrome()
driver.minimize_window()
mylist = ["tiket.com","tokopedia.com","orangsiber.com","demoqa.com","automatetheboringstuff.com"]

for i in mylist:
    driver.get("https://"+i)
    print(f"{i} - {driver.title}")

driver.close()