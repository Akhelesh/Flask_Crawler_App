import time
import requests
from celery.exceptions import SoftTimeLimitExceeded
from pycrawler.crawler.create_crawler import CreateCrawler
from pycrawler import celery
from .utils import send_email


# Request after every 20 minutes
TIME_PERIOD = 1200

crawler = None


@celery.task(name='tasks.run_crawler', soft_time_limit=86400)
def run_crawler(email, domain, name):
    global crawler
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


@celery.task(name='tasks.keep_heroku_alive', soft_time_limit=86400)
def keep_heroku_alive(t):
    global crawler
    time.sleep(15)
    while crawler.finished is False:
        print('__KEEP ALIVE REQUEST__')
        time.sleep(t)
        requests.get('https://pycrawler.herokuapp.com/')
