from selenium import webdriver
import time

browser = webdriver.Chrome(r'C:\Users\Yuri\Desktop\chromedriver.exe')

frequency = 10

mobile_number = ""

for i in range(frequency):
    browser.get('https://www.flipkart.com/account/login?ret =/')
    number = browser.find_element_by_class_name('_2zrpKA')
    number.send_keys("")
    forgot = browser.find_element_by_link_text('Forgot?')
    forgot.click()
    time.sleep(10)


browser.quit()
