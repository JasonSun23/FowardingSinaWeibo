from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, pymongo
from Cookie import SimpleCookie

driver = webdriver.Firefox()
login_url = "https://login.sina.com.cn/signup/signin.php?entry=sso"
driver.get(login_url)
time.sleep(5)

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
smb_btn = driver.find_element_by_class_name('btn_submit_m')
safe_login = driver.find_element_by_id('safe_login')

username.send_keys('username123')
password.send_keys('password123')

safe_login.click()
time.sleep(2)
smb_btn.click()
time.sleep(5)

clinet = pymongo.MongoClient("localhost", 27017)
db = clinet["Tweets"]
tweets = db["Tweets"]

for tweet in tweets.find():
    tweet_id = tweet["_id"][2:]
    user_id = tweet["ID"]
    tweet_url = "http://weibo.cn/repost/%s?uid=%s&rl=1" % (tweet_id, user_id)

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    time.sleep(5)

    driver.get(tweet_url)
    time.sleep(5)

    text = driver.find_element_by_id('content')
    text.send_keys(u'\u8f6c\u53d1\u62bd\u5956')
    time.sleep(5)
    send = driver.find_element_by_xpath("//input[@type='submit']")
    send.click()
    time.sleep(5)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    time.sleep(1)