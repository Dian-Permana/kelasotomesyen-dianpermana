from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.close()

def test_login_OK(setup):
    """
    login dengan menggunakan username dan password yang benar
    """
    setup.find_element(By.NAME,"username").send_keys("Admin") #username
    setup.find_element(By.NAME,"password").send_keys("admin123") #password
    setup.find_element(By.XPATH,"//button[@type='submit']").click() #button login

    title = setup.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    assert title == "Dashboard"

input_output = [
    ("Admin", "admin1234", True, "Invalid credentials"),
    ("Udin", "admin123", True, "Invalid credentials"),
    ("Udin", "admin1234", True, "Invalid credentials")]

@pytest.mark.parametrize("username, password, notifikasi, notifikasi_text", input_output)

def test_login_NG(setup, username, password, notifikasi, notifikasi_text):
    """
    login dengan menggunakan username dan password yang salah
    """
    setup.find_element(By.NAME,"username").send_keys(username) #username
    setup.find_element(By.NAME,"password").send_keys(password) #password
    setup.find_element(By.XPATH,"//button[@type='submit']").click() #button login

    notification_error = setup.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").is_displayed()
    notification_text = setup.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

    assert notification_error == notifikasi
    assert notification_text == notifikasi_text
