from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Observe result: print(soup)

# Find body tag: print(soup.find('body'))

# Print script: print(soup.find('script', id = "__NEXT_DATA__"))
import json
'''
data = soup.find('script', id = "__NEXT_DATA__").text
content = json.loads(data)["props"]["pageProps"]["page"]["@\"news\","]["sections"]
titles = [line['title'] for line in content[0]["content"]]
print(titles)
'''


























# API
def getMainTitle():
    # Set Chrome options
    options = Options()
    options.add_argument("--headless")

    # Use Service properly
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Step 1: Open BBC news
    url = 'https://www.bbc.com/news'
    driver.get(url)

    # Step 2: Get the full HTML of the results page
    html = driver.page_source

    # Step 3: Close the browser
    driver.quit()


    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    data = soup.find('script', id = "__NEXT_DATA__").text
    content = json.loads(data)["props"]["pageProps"]["page"]["@\"news\","]["sections"]
    titles = [line['title'] for line in content[0]["content"]]
    return titles