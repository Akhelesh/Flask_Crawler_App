from pycrawler.crawler.create_crawler import CreateCrawler
from .celery import app


@app.task(name='tasks.run_crawler')
def run_crawler(domain, name):
    crawler = CreateCrawler(domain, name)
    crawler.create_threads()
    crawler.run_crawl()
