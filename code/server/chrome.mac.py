# coding:utf-8
import os, time, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 環境変数の設定
import config as conf

def get_screen_shot(driver):
    dt = datetime.datetime.today()
    now = dt.strftime('%Y%m%d%H%M%S')
    return driver.save_screenshot(f'images/{now}.png')


def chrome(driver, get_url: str):
    driver.get(get_url)
    # ログイン
    driver.find_element_by_id('user_email').send_keys(conf.WANTEDLY_ID)
    driver.find_element_by_id('user_password').send_keys(conf.WANTEDLY_PASSWORD)
    driver.find_element_by_name('commit').click()
    time.sleep(2)
    # メッセージ
    driver.get('https://www.wantedly.com/enterprise/messages')
    time.sleep(2)
    # 全てのメッセージ
    driver.find_element_by_xpath('//li[contains(text(), "すべてのメッセージ")]').click()
    time.sleep(2)
    return
    # 応募者一覧を取得
    # user_list = driver.find_elements_by_class_name('MessageThreadListItem--date')
    # time.sleep(2)
    # user_name_list = []
    # for user in user_list:
    #     name = user.find_element_by_tag_name('a')
    #     time.sleep(1)
    #     user_name_list.append(name.text)



if __name__ == '__main__':

    url: str = 'https://www.wantedly.com/user/sign_in'

    # ドライバ取得
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(conf.CHROMEDRIVER, options=options)

    # 処理
    try:
        chrome(driver, url)

    except Exception as e:
        print(e)

    finally:
        time.sleep(100)
        driver.quit()
