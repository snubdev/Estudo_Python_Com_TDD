from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=servico)

browser.get('http://localhost:8000')
sleep(10)

#assert 'Django' in browser.title
