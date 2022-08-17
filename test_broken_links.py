""" This is for checking test link broken and check Pylint ... Trailing"""
from selenium.webdriver import Chrome
from requests import request

driver = Chrome(r"F:\PyCharm Files\Framework\Data\chromedriver.exe")
driver.get("https://www.google.com")

# Find all the elements
links = driver.find_elements_by_xpath("//a")

# Iterate through the list and get the value of "href" attribute
urls = []

for link in links:
    urls.append(link.get_attribute("href"))

for url in urls:
    print(f"Hitting url : {url}")
    response = request("Get", url)
    if response.status_code == 200:
        print("PASS")
    else:
        print(f"FAIL : Broken Link{url}")

# pylint test_broken_link.py
