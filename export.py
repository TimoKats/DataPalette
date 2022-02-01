import requests
from bs4 import BeautifulSoup

global_soup = ""

def make_global_soup(url):
    global global_soup
    page = requests.get(url)
    global_soup = BeautifulSoup(page.content, 'html.parser')



def item_check(items):
    if len(items) > 1:
        return items
    elif len(items) == 1:
        return items[0]
    else:
        return 'NULL'

def export_metacontent(property):
    metatags = global_soup.find_all('meta')
    items = []
    for tag in metatags:
        if property in str(tag) and len(tag) < len(metatags):
            items.append(tag['content'])
    return item_check(items)

def export_metahtml(property):
    metatags = global_soup.find_all('meta')
    items = []
    for tag in metatags:
        if property in str(tag) and len(tag) < len(metatags):
            items.append(str(tag))
    return item_check(items)