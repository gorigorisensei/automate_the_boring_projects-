from selenium import webdriver
PATH = r"/usr/local/bin/chromedriver"
browser = webdriver.Chrome(PATH)
browser.get("https://automatetheboringstuff.com/")
