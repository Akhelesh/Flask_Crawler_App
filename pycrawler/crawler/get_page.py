import requests
from bs4 import BeautifulSoup


class GetPage:
    def __init__(self, url):
        self.url = url
        self.content = ''
        self.links = []

    def get(self):
        """
        Get all links pointing to same domain from a page

        :param page: link for the page for which to find links
        """
        try:
            html = requests.get(self.url).content
            soup = BeautifulSoup(html, 'lxml')

    #       Extract script and styles from soup to get clean text
            for script in soup(['script', 'style']):
                script.extract()
            text = soup.getText()
            lines = [line.strip() for line in text.splitlines()]
            chunks = [chunk.strip() for line in lines for chunk in line.split(' ')]
            self.content = ' '.join(chunks)

    #        Extract links from the soup
            for link in soup.find_all('a', href=True):
                self.links.append(link['href'])
        except:
            pass
