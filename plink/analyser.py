import requests
from bs4 import BeautifulSoup

def retrieve_content_by_url(url):
    request = requests.get(url)
    content = request.text
    return content

def retrieve_links_from_html(html):
    soup = BeautifulSoup(html, 'html')
    link_tags = soup.find_all('a')
    links = [tag['href'] for tag in link_tags]
    print(links)

def analyse(options):
    print("Analysing")
    print(options.start_url)
    content = retrieve_content_by_url(options.start_url)
    retrieve_links_from_html(content)