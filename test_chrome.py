#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--ignore-certificate-errors")
#options.add_argument("--incognito")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
#options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--enable-file-cookies")
#options.add_argument("--enable-experimental-cookie-features")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

# This test will run when 'login_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "login_test"'.
# This test will run when 'empty_form_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
@pytest.mark.browser_test
def test_assert_empty_login_form():
    browser.get('https://myevesachinsp1651776534764.dashboard.psonar.us/login')
    assert "Welcome to Prosimo" in browser.page_source, broswer.page_source
