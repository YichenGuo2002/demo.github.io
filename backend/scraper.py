import requests
from bs4 import BeautifulSoup

# Target URL
url = 'https://en.wikipedia.org/wiki/Dublin'

# Send GET request
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    # Pirnt HTML print(soup)

    # Print all i tag print(soup.find_all('i'))

    # Print first i print(soup.find('i'))

    # Or you can do print(soup.find_all('i')[0])

    # To print text print(soup.find_all('i')[0].text)

    # Finding motto by classname print(soup.find_all('div', class_ = 'ib-settlement-nickname nickname'))

    # We need the second one print(soup.find_all('div', class_ = 'ib-settlement-nickname nickname')[1].text)

    # Not this one? Find the nearest tag! print(soup.find_all('div', class_ = 'ib-settlement-nickname nickname')[1].find('i').text)

    # Web crawling: print([i['href'] if i.has_attr('href') else '' for i in soup.find_all('a')])

    # How about external links:
    '''
    links = [i['href'] if i.has_attr('href') else '' for i in soup.find_all('a')]
    for link in links:
        if link.startswith('http') or link.startswith('www'):
            print(link)
    '''

    # Anything else to print?
    
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
