from pages.login_page import LoginPage
from playwright.sync_api import expect
import pytest

def test_successful_login(page):
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username,password)

    assert "Swag Labs" in page.title()

def test_page_url(page):
    login_page=LoginPage(page)
    login_page.open()

    assert page.url == "https://www.saucedemo.com/"

def test_find_error_message_element(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.attempt_login("locked_out_user", "secret_sauce")

    expect(
        login_page.get_error_message()
    ).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("wrong_user","secret_sauce",
         "Epic sadface: Username and password do not match any user in this service"),

        ("standard_user","wrong_password",
         "Epic sadface: Username and password do not match any user in this service"),

        ("","secret_sauce",
         "Epic sadface: Username is required"),

        ("standard_user","",
         "Epic sadface: Password is required"),

        ("","",
         "Epic sadface: Username is required"),

        ("locked_out_user","secret_sauce",
         "Epic sadface: Sorry, this user has been locked out."),
    ],
    ids=[
        "invalid_username",
        "invalid_password",
        "empty_username",
        "empty_password",
        "empty_username_and_password",
        "locked_user"

    ],
)
def test_invalid_login(page,username,password,expected_error):
    login_page = LoginPage(page)
    login_page.open()
    login_page.attempt_login(username,password)

    expect(login_page.get_error_message()).to_have_text(expected_error)


