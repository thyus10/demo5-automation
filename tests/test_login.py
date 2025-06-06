from playwright.sync_api import Page,expect
import pytest
from pages.login_page import LoginPage


def test_login_tc_01(set_up_tear_down) -> None:
    page = set_up_tear_down
    credentials = {'email': 'jisoo@yopmail.com', 'password': 'jisookim'}

    login_p = LoginPage(page)
    login_p.do_login(credentials)
