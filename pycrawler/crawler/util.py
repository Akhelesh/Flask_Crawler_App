import os
import requests
from bs4 import BeautifulSoup


DATA_DIR_PATH = 'data'


def create_dir(dir_name):
    path = os.path.join(DATA_DIR_PATH, dir_name)
    if not os.path.exists(path):
        os.makedirs(path)


def create_files(dir_name, base_url):
    queue_file = os.path.join(DATA_DIR_PATH, dir_name, 'queue.txt')
    crawled_file = os.path.join(DATA_DIR_PATH, dir_name, 'crawled.txt')
    external_file = os.path.join(DATA_DIR_PATH, dir_name, 'external.txt')

    if not os.path.exists(queue_file):
        write_to_file(queue_file, base_url)
    if not os.path.exists(crawled_file):
        write_to_file(crawled_file, '')
    if not os.path.exists(external_file):
        write_to_file(external_file, '')


def write_to_file(file, data):
    with open(file, 'w') as f:
        f.write(data + "\n")


def get_links_from_file(file):
    links = set()
    path = os.path.join(DATA_DIR_PATH, file)
    with open(path, 'r') as f:
        for link in f:
            if link:
                links.add(link.replace("\n", ''))
    return links


def save_links_to_file(file, links):
    path = os.path.join(DATA_DIR_PATH, file)
    with open(path, 'w') as f:
        for link in links.copy():
            if link:
                f.write(link + "\n")


def get_text_from_file(file):
    with open(file, 'r') as f:
        return f.read()


def get_page(url):
        links = []
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
        try:
            html = requests.get(url, headers=headers).content
            soup = BeautifulSoup(html, 'lxml')

            for link in soup.find_all('a', href=True):
                links.append(link['href'])
        except Exception:  # Skip link if unable to get it
            pass

        return links
