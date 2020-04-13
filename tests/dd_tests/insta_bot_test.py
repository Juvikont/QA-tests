# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
#
# class InstagramBot():
#     def __init__(self, email, password):
#         self.browserProfile = webdriver.ChromeOptions()
#         self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
#         self.browser = webdriver.Chrome(r'C:\Users\Yuri\Desktop\chromedriver.exe', chrome_options=self.browserProfile)
#         self.email = email
#         self.password = password
#
#     def signIn(self):
#         self.browser.get('https://www.instagram.com/accounts/login/')
#
#         emailInput = self.browser.find_elements_by_css_selector('form input')[0]
#         passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
#
#         emailInput.send_keys(self.email)
#         passwordInput.send_keys(self.password)
#         passwordInput.send_keys(Keys.ENTER)
#         time.sleep(2)
#
#     def followWithUsername(self, username):
#         self.browser.get('https://www.instagram.com/' + username + '/')
#         time.sleep(2)
#         followButton = self.browser.find_element_by_css_selector('button')
#         if (followButton.text != 'Following'):
#             followButton.click()
#             time.sleep(2)
#         else:
#             print("You are already following this user")
#
#     def unfollowWithUsername(self, username):
#         self.browser.get('https://www.instagram.com/' + username + '/')
#         time.sleep(2)
#         followButton = self.browser.find_element_by_css_selector('button')
#         if (followButton.text == 'Following'):
#             followButton.click()
#             time.sleep(2)
#             confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
#             confirmButton.click()
#         else:
#             print("You are not following this user")
#
#     def getUserFollowers(self, username, max):
#         self.browser.get('https://www.instagram.com/' + username)
#         followersLink = self.browser.find_element_by_css_selector('ul li a')
#         followersLink.click()
#         time.sleep(2)
#         followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
#         numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#
#         followersList.click()
#         actionChain = webdriver.ActionChains(self.browser)
#         while (numberOfFollowersInList < max):
#             actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
#             numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
#             print(numberOfFollowersInList)
#
#         followers = []
#         for user in followersList.find_elements_by_css_selector('li'):
#             userLink = user.find_element_by_css_selector('a').get_attribute('href')
#             print(userLink)
#             followers.append(userLink)
#             if (len(followers) == max):
#                 break
#         return followers
#
#     def closeBrowser(self):
#         self.browser.close()
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.closeBrowser()
#
# InstagramBot.getUserFollowers()
#

a = 'Сэм шел через лес, он заметил несколько птиц, летающих у него над головой и сидящих на ветках. Это его не удивило, так как была середина лета. Был только еще один знак того, что что-то очень странное произошло здесь недавно. Он решил узнать, что же это было.'
a = a.lower()
print(a.count('у'))

# n = 60
# x = 555
#
# b = x // n
# p = x%n
# print(b)
# print(p)
