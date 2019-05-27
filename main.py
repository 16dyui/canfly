#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/c/Users/maruyama/Documents/bin/chromedriver.exe")
driver.implicitly_wait(20)

for i in range(100):
    driver.get('https://spend.ponta.jp/Form/Product/ProductDetail.aspx?pid=LN-000001')
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_lbCartAdd").click()
    driver.find_element_by_css_selector("#CartList .next>a").click()
    driver.find_element_by_css_selector("#RID_BLOCK .rid-login-box>a").click()
    if(i==0):
        driver.find_element_by_name("mainEmail").send_keys("") #リクルートアカウント
    driver.find_element_by_name("passwd").send_keys("") #リクルートパスワード
    driver.find_element_by_css_selector("[name='member_pwbOAuthLoginActionForm'] .btnAction01_LV01Lg").click()
    #メール認証
    if(i==0):
        driver.execute_script("window.open('http://mail.google.com/mail/?ui=html&zy=e')")
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_name("identifier").send_keys("") #gmailアカウント
        driver.find_element_by_id("identifierNext").click()
        driver.find_element_by_name('password').send_keys("") #gmailパスワード
        time.sleep(1)
        driver.find_element_by_id("passwordNext").click()
        driver.find_element_by_css_selector("form>table:nth-of-type(2) tr:first-of-type a").click()
        m = re.search(r"\d+", driver.find_element_by_css_selector(".msg").text).group()
        driver.find_element_by_name("nvp_a_tr").click()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_name("addauthConfirmCd").send_keys(m)
        driver.find_element_by_id("sbmbtn").click()
    #メール認証終了

    driver.find_element_by_css_selector("#contents .next>a").click()
    driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_upUpdatePanel .next>a").click()
    driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_lbComplete2").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.refresh()
    driver.find_element_by_css_selector("form>table:nth-of-type(2) tr:first-of-type a").click()
    t = re.findall(r"\d+", driver.find_element_by_css_selector(".msg").text)[-1]
    driver.find_element_by_name("nvp_a_tr").click()
    if(i==0):
        driver.execute_script("window.open('https://points.line.me/pointcode/#/pointcode/form')")
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element_by_name("pincode").send_keys(t)
    driver.find_element_by_tag_name("button").click()
    driver.find_element_by_name("tid").send_keys("") #LINEアカウント
    driver.find_element_by_name("tpasswd").send_keys("") #LINEパスワード
    driver.find_element_by_css_selector("[type='submit']").click()
    driver.find_element_by_tag_name("a").click()
    driver.switch_to.window(driver.window_handles[0])
