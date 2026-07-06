import os
import pytest

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
STORAGE_STATE_PATH = "storage_state.json"


@pytest.fixture(scope="session")
def storage_state_path(browser):
    """Log in once per test session and persist the authenticated state to disk."""
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    page.locator('[data-test="username"]').fill(USERNAME)
    page.locator('[data-test="password"]').fill(PASSWORD)
    page.locator('[data-test="login-button"]').click()
    page.wait_for_url("**/inventory.html")
    context.storage_state(path=STORAGE_STATE_PATH)
    context.close()

    yield STORAGE_STATE_PATH

    os.remove(STORAGE_STATE_PATH)


@pytest.fixture
def authenticated_page(browser, storage_state_path):
    """A page whose browser context is already logged in, starting on the inventory page."""
    context = browser.new_context(storage_state=storage_state_path)
    page = context.new_page()
    page.goto(f"{BASE_URL}inventory.html")

    yield page

    context.close()
