import time

from selenium import webdriver

print('Enter username: ')
username = input()

print('Enter password: ')
password = input()

print('Enter the url: ')
url = input()


def path():
    """webdriver path finder"""
    global chrome
    print('Enter driver path')
    exe_path = input()
    # start's new session
    chrome = webdriver.Chrome(executable_path=exe_path)


def url_name(url):
    """web page opens up"""
    chrome.get(url)
    # wait 4 sec
    time.sleep(4)


def login(username, your_password):
    """login func"""
    log_but = chrome.find_element_by_class_name("L3NKy")  # login button finder
    log_but.click()  # clicks log_but
    time.sleep(4)
    usern = chrome.find_element_by_name('username')  # username box finder
    usern.send_keys(username)  # sends username
    passw = chrome.find_element_by_name('password')  # password box finder
    passw.send_keys(your_password)  # sends password
    log_cl = chrome.find_element_by_class_name('L3NKy')  # finds and clicks login button
    log_cl.click()
    time.sleep(4)


def first_picture():
    """first pic finder"""
    pic = chrome.find_element_by_class_name('_9AhH0')
    pic.click()


def like_pic():
    """like button finder and clicker"""
    time.sleep(4)
    like = chrome.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')

    time.sleep(2)
    like.click()


def next_picture():
    """next button finder"""
    time.sleep(2)
    nex = chrome.find_element_by_class_name('HBoOv')
    time.sleep(1)
    return nex


def liker():
    """the liker"""
    while (True):
        next_element = next_picture()
        if next_element != False:
            next_element.click()
            time.sleep(2)
            like_pic()
            time.sleep(2)
        else:
            print('not found')
            break


path()
time.sleep(1)

url_name(url)
login(username, password)

first_picture()
like_pic()

liker()
