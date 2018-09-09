from tldextract import extract
from pycrawler.crawler.util import *
from pycrawler.crawler.get_page import GetPage


class Crawler:
    def __init__(self, domain, crawler_name):
        self.name = crawler_name
        self.domain = domain
        self.queue = set()
        self.crawled = set()
        self.external = set()
        self.queue_file = self.name + '/queue.txt'
        self.crawled_file = self.name + '/crawled.txt'
        self.external_file = self.name + '/external.txt'
        self.setup_crawler()
        self.crawl(self.domain)

    def setup_crawler(self):
        create_dir(self.name)
        create_files(self.name, self.domain)
        self.queue = get_links_from_file(self.queue_file)
        self.crawled = get_links_from_file(self.crawled_file)

    def crawl(self, url):
        if url not in self.crawled and self.verify_domain(url):
            print('Crawler instance - currently @', url)
            try:
                page_getter = GetPage(url)
                page_getter.get()
                links = set(page_getter.links)
                links = self.parse_urls(links)
                self.add_links_to_queue(links)
                self.get_external_links(links)
                self.queue.remove(url)
                self.crawled.add(url)
                self.update_files()
            except Exception as e:
                print(e)
                self.queue.remove(url)
                self.update_files()

    def update_files(self):
        save_links_to_file(self.queue_file, self.queue)
        save_links_to_file(self.crawled_file, self.crawled)
        save_links_to_file(self.external_file, self.external)

    def add_links_to_queue(self, links):
        for l in links:
            if (l in self.crawled) or (l in self.queue)\
            or (not self.verify_domain(l)):
                continue
            self.queue.add(l)

    def verify_domain(self, url):
        domain_nloc = extract(self.domain).domain
        url_nloc = extract(url).domain
        if domain_nloc == url_nloc:
            return True
        return False

    def get_external_links(self, links):
        for l in links:
            if not self.verify_domain(l):
                self.external.add(l)

    def parse_urls(self, links):
        parsed_links = set()
        for l in links:
            if 'http' in l:
                parsed_links.add(l.split('#')[0])

        return parsed_links
