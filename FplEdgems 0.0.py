"""
test edge browser
"""
from selenium import webdriver
if __name__ == '__main__':
	# Instantiate the webdriver with the executable location of MS Edge web driver
	browser = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
	# Simply just open a new Edge browser and go to fpl page.
	browser.maximize_window()
	browser.get('https://fantasy.premierleague.com/')
