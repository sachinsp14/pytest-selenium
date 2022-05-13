#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()


# This test will run when 'login_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "login_test"'.
# This test will run when 'empty_form_test' is called when invoking -m,
# e.g. 'pytest test_custom_markers.py -m "empty_form_test"'.
@pytest.mark.broswer_test
def test_assert_empty_login_form():
    browser.get(https://myevesachinsp1651776534764.dashboard.psonar.us/login)
    assert "Welcome to Prosimo" in broswer.page_source
