
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def login(driver, username=USERNAME, password=PASSWORD):
    driver.get(URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def test_TC01_login_success(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    assert "/inventory.html" in driver.current_url
    assert driver.find_element(
        By.CLASS_NAME, "title"
    ).text == "Products"


def test_TC02_login_invalid_password(driver):
    login(driver, USERNAME, "wrong_password")

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    )

    assert "Username and password do not match" in error.text


def test_TC03_sort_products_by_price(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    sort_dropdown = Select(
        driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )
    )
    sort_dropdown.select_by_value("lohi")

    prices = [
        float(item.text.replace("$", ""))
        for item in driver.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )
    ]

    assert len(prices) > 0
    assert prices == sorted(prices)


def test_TC04_add_product_to_cart(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert badge.text == "1"

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    cart_items = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(cart_items) == 1
    assert "Sauce Labs Backpack" in driver.page_source


def test_TC05_logout(driver):
    login(driver)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )

    driver.find_element(
        By.ID, "react-burger-menu-btn"
    ).click()

    logout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )
    )
    logout.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        )
    )

    assert driver.find_element(
        By.ID, "login-button"
    ).is_displayed()
