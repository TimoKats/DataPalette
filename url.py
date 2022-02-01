import requests
from bs4 import BeautifulSoup

def get_linked_urls(url, substring):
    links = []
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
    else:
        return

    if len(soup.find_all('a')) > 0:
        for link in soup.find_all('a'):
            if substring == "":
                if link.get('href')[0] == "/":
                    links.append(str(url + link.get('href')))
                else:
                    links.append(link.get('href'))
            elif substring in link.get('href'):
                if link.get('href')[0] == "/":
                    links.append(str(url + link.get('href')))
                else:
                    links.append(link.get('href'))
    return links