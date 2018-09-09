from pycrawler.crawler.create_crawler import CreateCrawler
from pycrawler import celery
from .utils import send_email

crawler = None


@celery.task(name='tasks.run_crawler')
def run_crawler(email, domain, name):
    global crawler
    crawler = CreateCrawler(domain, name)
    crawler.create_threads()
    crawler.run_crawl()
    if crawler.finished:
        crawler.add_to_database()
        send_email(email, name)
