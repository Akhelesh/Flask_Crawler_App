import threading
from queue import Queue
from pycrawler import db
from pycrawler.models import Domain
from pycrawler.crawler.util import *
from pycrawler.crawler.crawler import Crawler


class CreateCrawler:
    NUMBER_OF_THREADS = 4

    def __init__(self, domain, name):
        self.crawler = Crawler(domain, name)
        self.queue = Queue()
        self.finished = False

    def create_threads(self):
        for _ in range(CreateCrawler.NUMBER_OF_THREADS):
            thread = threading.Thread(target=self.work, daemon=True)
            thread.start()

    def work(self):
        while True:
            url = self.queue.get()
            print('Crawling', url)
            self.crawler.crawl(url)
            self.queue.task_done()

    def populate_queue(self):
        for link in get_links_from_file(self.crawler.queue_file):
            if link:
                self.queue.put(link)
        self.queue.join()

    def run_crawl(self):
        queue_links = get_links_from_file(self.crawler.queue_file)
        while len(queue_links) > 0:
            self.populate_queue()
            queue_links = get_links_from_file(self.crawler.queue_file)
        self.finished = True

    def add_to_database(self):
        domain = Domain(domain_name=self.crawler.name,
                        url=self.crawler.domain)
        db.session.add(domain)
        db.session.commit()
