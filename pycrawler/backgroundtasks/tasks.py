import time
import requests
from celery.exceptions import SoftTimeLimitExceeded
from pycrawler.crawler.create_crawler import CreateCrawler
from .celery import celery
from .utils import send_email


@celery.task(name='tasks.run_crawler', soft_time_limit=86400)
def run_crawler(email, domain, name):
    crawler = CreateCrawler(domain, name)
    try:
        crawler.create_threads()
        crawler.run_crawl()
        if crawler.finished:
            crawler.add_to_database()
            send_email(email, name)
    except SoftTimeLimitExceeded:
        crawler.add_to_database()
        send_email(email, name)
