# FowardingSinaWeibo
爬取新浪微博的抽奖微博，并自动转发

## 爬取微博
爬取新浪微博参考了https://github.com/LiuXingMing/SinaSpider
主要原理就是爬取某些VIP用户(可扩展)前一天的微博里是否含有抽奖信息，若有，则将该微博信息存入MongoDB数据库。
运行 python Begin.py

## 转发微博
转发抽奖微博利用Selenium中的WebDriver，登录微博并读取MongoDB里的微博信息，实施自动转发。可扩展为多用户进行转发，以增加中奖概率。
运行 python repost.py
