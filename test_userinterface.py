import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

def test_cookies_div_properties(driver):
    wait = WebDriverWait(driver, 10)
    eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))

    background_color = eleCookiesDiv.value_of_css_property("background-color")
    height = float(eleCookiesDiv.size['height'])
    width = eleCookiesDiv.value_of_css_property("width")

    assert background_color == "rgba(255, 0, 0, 1)", f"Expected rgba(255, 0, 0, 1), but got {background_color}"
    assert height == 175.0, f"Expected height 175.0, but got {height}"
    assert width == '300px', f"Expected width '300px', but got {width}"

def test_logo_dimensions(driver):
    wait = WebDriverWait(driver, 10)
    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo_icon')))

    height = float(logo.size['height'])
    width = float(logo.size['width'])

    assert height == 175.0, f"Expected height 175.0 px, but got {height} px"
    assert width == 300.0, f"Expected width 300.0 px, but got {width} px"

def test_password_field_dimensions(driver):
    wait = WebDriverWait(driver, 10)
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))

    width = float(password_field.size['width'])
    height = float(password_field.size['height'])

    assert width == 372.0, f"Expected width 372.0 px, but got {width} px"
    assert height == 40.0, f"Expected height 40.0 px, but got {height} px"

def test_email_field_dimensions_and_font(driver):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))

    width = float(email_field.size['width'])
    font_family = email_field.value_of_css_property("font-family")

    assert width == 133.688, f"Expected width 133.688 px, but got {width} px"
    assert "sans-serif" in font_family, f"Expected font family to include 'sans-serif', but got {font_family}"

def test_email_field_height(driver):
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))

    height = float(email_field.size['height'])

    assert height == 40.0, f"Expected height 40.0 px, but got {height} px"

def test_domain_field_dimensions(driver):
    wait = WebDriverWait(driver, 10)
    domain_field = wait.until(EC.visibility_of_element_located((By.NAME, 'domain')))

    width = float(domain_field.size['width'])
    height = float(domain_field.size['height'])

    assert width == 133.688, f"Expected width 133.688 px, but got {width} px"
    assert height == 40.0, f"Expected height 40.0 px, but got {height} px"

def test_font_size(driver):
    wait = WebDriverWait(driver, 10)
    any_element = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))  # Adjust the selector as needed

    font_size = any_element.value_of_css_property("font-size")

    assert font_size == "14.4px", f"Expected font size 14.4 px, but got {font_size}"
