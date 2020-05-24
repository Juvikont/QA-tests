from selenium import webdriver
from tests.selenium_insta import bot_engine

chromedriver_path = r'C:\Users\Yuri\Desktop\chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

bot_engine.init(webdriver)
bot_engine.update(webdriver)

webdriver.close()
