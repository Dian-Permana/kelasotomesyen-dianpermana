from selenium import webdriver
import pytest
from pages.login_page import Login
from pages.inventory_page import Inventory
from locators.login import LocLogin

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()

def test_login_positif(setup):
    '''
    Login dengan menggunakan username dan password yang benar
    '''
    login = Login(setup)
    inventory = Inventory(setup)
    
    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()
    
    title = inventory.check_title()

    assert title == 'Swag Labs'
    
@pytest.mark.parametrize('username, password, notifikasi, notiftext',LocLogin.input_output)
def test_login_negatif_1(setup, username, password, notifikasi, notiftext):
    '''
    Login dengan menggunakan username yang salah dan password yang benar
    
    username password result

    salah    bener    gak bisa login
    bener    salah    gak bisa login
    salah    salah    gak bisa login
    
    '''
    login = Login(setup)
    inventory = Inventory(setup)

    login.input_username(username)
    login.input_password(password)
    login.click_login_button()

    error = login.check_notifikasi()
    assert error == notifikasi

    text = login.text_notifikasi()
    assert text == notiftext