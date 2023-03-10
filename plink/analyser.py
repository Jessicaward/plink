import requests
import urllib.parse
from bs4 import BeautifulSoup

def retrieve_content_by_url(url):
    request = requests.get(url)
    content = request.text
    return content

def retrieve_links_from_html(html, base_url):
    soup = BeautifulSoup(html, features="html.parser")
    link_tags = soup.find_all('a')
    links = [tag['href'] for tag in link_tags]
    absolute_links = [urllib.parse.urljoin(base_url, link) for link in links]
    return absolute_links

def analyse_url(url):
    content = retrieve_content_by_url(url)
    links = retrieve_links_from_html(content, url)

    #todo: also return status code?
    return links

def analyse(options):
    print(analyse_url(options.start_url))