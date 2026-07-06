# SauceDemo Playwright Automation

Page Object Model test suite for https://www.saucedemo.com, built with Playwright + pytest.

## Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    playwright install

## Running tests

    pytest -q

Run a single file:

    pytest tests/test_login_page.py -q

## Structure

- `pages/` — Page Object classes, one per page
- `tests/` — test files, one per page, plus `conftest.py` for shared fixtures
- `data/` — static test data (e.g. checkout address fields)