# coding:utf-8
import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys


options = Options()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome('chromedriver', chrome_options=options)
# ブラウザを開く
driver.get('https://www.yahoo.co.jp/')
driver.save_screenshot('./screenshot.png')
driver.quit()

# # 3秒待機
# time.sleep(3)
# # ログインボタンをクリックする
# login_btn = driver.find_element_by_xpath('//*[@id="Login"]/div/p[1]/a')
# login_btn.click()
# # 1秒待機
# time.sleep(1)
# # ログインIDを入力
# login_id = driver.find_element_by_name("login")
# login_id.send_keys("yuya_yamada00@yahoo.co.jp")
# # 次へボタンをクリック
# next_btn = driver.find_element_by_name("btnNext")
# next_btn.click()
# # 1秒待機
# time.sleep(1)
# # パスワードを入力
# password = driver.find_element_by_name("passwd")
# password.send_keys("Einstein1538yahoo")
# #ログインボタンをクリック
# login_btn = driver.find_element_by_name("btnSubmit")
# login_btn.click()
# #10秒待機
# time.sleep(10)
# # ブラウザを終了する。
# driver.close()
