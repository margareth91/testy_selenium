
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# arrange
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://testuj.pl')
# driver.get('https://google.pl')
# act
title = driver.title
# assert
assert title == "Zostań certyfikowanym testerem. Kursy z testowania oprogramowania • testuj.pl"
