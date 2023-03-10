import requests
import urllib.parse
from bs4 import BeautifulSoup
from result import Result
from termcolor import colored

class Analyser():
    def __init__(self, options):
        self.options = options

    def retrieve_content_by_url(self, url):
        request = requests.get(url)
        content = request.text
        return content

    def retrieve_links_from_html(self, html, base_url):
        soup = BeautifulSoup(html, features="html.parser")
        link_tags = soup.find_all('a')
        links = [tag['href'] for tag in link_tags]
        absolute_links = [urllib.parse.urljoin(base_url, link) for link in links]
        return absolute_links

    def analyse_url(self, url, depth):
        try:
            content = self.retrieve_content_by_url(url)
            links = self.retrieve_links_from_html(content, url)
            print(colored((depth * "  ") + "Success: " + url, "green"))
            return Result(links=links, status="Success")
        except Exception as ex:
            if self.options.verbose:
                print(colored((depth * "  ") + str(ex), "red"))
            print(colored((depth * "  ") + "Fail: " + url, "red"))
            return Result(status="Fail")

    def analyse(self):
        analysed_urls = []
        urls_to_analyse = [self.options.start_url]
        for depth in range(0, self.options.recursion_depth):
            urls_in_step = urls_to_analyse[:] # Copy list without reference
            for url in urls_in_step:
                result = self.analyse_url(url, depth)
                analysed_urls.append(url)
                urls_to_analyse.remove(url)
                for url_to_analyse in result.links:
                    if url_to_analyse not in urls_to_analyse:
                        urls_to_analyse.append(url_to_analyse)