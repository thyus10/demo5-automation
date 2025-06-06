import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def set_up_tear_down():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1536, "height": 800})
        page = context.new_page()
        page.goto("https://demo5.cybersoft.edu.vn/login")

        credentials = {'email': 'jisookim@yopmail.com', 'password': 'jisookim'}

        login_p = LoginPage(page)
        login_p.do_login(credentials)

        print(f"URL sau khi đăng nhập: {page.url}")

        yield page

        context.close()
        browser.close()