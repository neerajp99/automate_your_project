# import pyautogui
# import sys

# # print(pyautogui.position())
# # print(pyautogui.size())
# # print(sys.argv[0])
# pyautogui.click(x=391, y=86, clicks=2)
# pyautogui.typewrite('hello') 
# pyautogui.typewrite(['enter'])


from selenium import webdriver
import pyautogui 
import time
import sys
import os

folderPath = "/path to your project/"
folderName = "mynewproject"
folderDescription = "test description"
githubUsername = 'githubUserName'
githubPassword = 'githubPassword'
isPrivate = 'private'
isReadme = 'readme'
isLicense = 'mit'
os.makedirs(folderPath + folderName)
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.github.com/login')
# pyautogui.click(x=454, y=422, clicks=3, interval=1)
github_login_field = browser.find_element_by_id("login_field")
github_login_field.send_keys(githubUsername)
github_password_field = browser.find_element_by_id("password")
github_password_field.send_keys(githubPassword)
browser.find_element_by_name("commit").click()
#allowing webpage to load, then redirect to new repo page
time.sleep(2)
browser.get('https://www.github.com/new')
github_repository_name = browser.find_element_by_id("repository_name").send_keys(folderName)
github_repository_description = browser.find_element_by_id("repository_description").send_keys(folderDescription)
if isPrivate == 'private':	
	browser.find_element_by_xpath("//*[@id='repository_visibility_private']").click()
if isReadme == 'readme':
	browser.find_element_by_xpath("//*[@id='repository_auto_init']").click()
browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button").click()

