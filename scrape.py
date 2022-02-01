import requests
import urllib.robotparser
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser')

def get_metacontent(url, property):
    soup = get_soup(url)
    metatags = soup.find_all('meta')
    items = ""
    for tag in metatags:
        if property in str(tag) and len(tag) < len(metatags):
            items += tag['content'] + "\n"
    return items

def get_metahtml(url, property):
    soup = get_soup(url)
    metatags = soup.find_all('meta')
    items = ""
    for tag in metatags:
        if property in str(tag) and len(tag) < len(metatags):
            items += str(tag) + "\n"
    return items

def get_meta(url):
    soup = get_soup(url)
    metatags = soup.find_all('meta')
    items = []
    for tag in metatags:
        for key, item in tag.attrs.items():
            if key != 'content':
                items.append(item)
    return ['meta properties'] + sorted(list(set(items)))