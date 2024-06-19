from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.minimize_window()
mylist = ["tiket.com","tokopedia.com","orangsiber.com","demoqa.com","automatetheboringstuff.com"]

for i in mylist:
    driver.get("https://"+i)
    print(f"{i} - {driver.title}")

driver.close()
