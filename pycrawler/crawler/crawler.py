from urllib.parse import urlparse
from pycrawler.crawler.util import *
from pycrawler.crawler.get_page import GetPage


class Crawler:
    def __init__(self, domain, crawler_name):
        self.crawler_name = crawler_name
        self.domain = domain
        self.queue = set()
        self.crawled = set()
        self.queue_file = self.crawler_name + '/queue.txt'
        self.crawled_file = self.crawler_name + '/crawled.txt'
        self.setup_crawler()
        self.crawl(self.domain)

    def setup_crawler(self):
        create_dir(self.crawler_name)
        create_files(self.crawler_name, self.domain)
        self.queue = get_links_from_file(self.queue_file)
        self.crawled = get_links_from_file(self.crawled_file)

    def crawl(self, url):
        if url not in self.crawled:
            print('Crawler instance - currently @', url)
            page_getter = GetPage(url)
            page_getter.get()
            links = set(page_getter.links)
            self.add_links_to_queue(links)
            self.queue.remove(url)
            self.crawled.add(url)
            self.update_files()

    def update_files(self):
        save_links_to_file(self.queue_file, self.queue)
        save_links_to_file(self.crawled_file, self.crawled)

    def add_links_to_queue(self, links):
        for link in links:
            if link not in self.crawled:
                self.queue.add(link)
