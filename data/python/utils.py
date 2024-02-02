import os
import requests
from bs4 import BeautifulSoup


class Downloader:
    def __init__(self):
        pass

    def download_image(self, url, folder_path, filename):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        response = requests.get(url, stream=True)
        with open(os.path.join(folder_path, filename), 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

class HTMLParser:
    def __init__(self, html_content):
        self.html_content = html_content
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extract_links(self):
        links = []
        for a_tag in self.soup.find_all('a', href=True):
            link = a_tag['href']
            links.append(link)
        return links
