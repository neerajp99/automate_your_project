from selenium import webdriver
import pyautogui
import time
import sys
import os

def init():
	# path to the folder where the project is to be created
	folderPath = "path to the directory"
	print(sys.argv)
	# name of the projecr
	folderName = str(sys.argv[1])
	# gihtub repository description
	folderDescription = str(sys.argv[2])
	# if the repository is private or public
	isPrivate = str(sys.argv[3])
	# to initialise a README file to the repository
	isReadme = str(sys.argv[4])
	# initialise github username and password
	githubUsername = 'githubUsername'
	githubPassword = 'githubPassword'
	# using os module to create a new directory for the project
	os.makedirs(folderPath + folderName)
	# open Chrome using webdriver
	browser = webdriver.Chrome()
	# maximize the chrome window
	browser.maximize_window()
	# launch github.com
	browser.get('https://www.github.com/login')
	# pyautogui.click(x = 454, y = 422, clicks = 3, interval = 1)
	# githuv username goes here
	github_login_field = browser.find_element_by_id("login_field")
	github_login_field.send_keys(githubUsername)
	# github password goes here
	github_password_field = browser.find_element_by_id("password")
	github_password_field.send_keys(githubPassword)
	# click the button to login
	browser.find_element_by_name("commit").click()
	# allowing webpage to load, then redirect to create github repository page
	time.sleep(2)
	# redirect to create repository page
	browser.get('https://www.github.com/new')
	# repository name goes here
	github_repository_name = browser.find_element_by_id("repository_name").send_keys(folderName)
	# repository description goes here
	github_repository_description = browser.find_element_by_id("repository_description").send_keys(folderDescription)
	# check if the repository is private and marks it
	if isPrivate == 'private':
	  browser.find_element_by_xpath("//*[@id='repository_visibility_private']").click()
	# check if readme is to be initialised and initialise it
	if isReadme == 'readme':
	  browser.find_element_by_xpath("//*[@id='repository_auto_init']").click()
	# button to proceed
	browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button").click()

if __name__ == "__main__":
  init()
