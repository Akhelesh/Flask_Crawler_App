import os


def parse_url(url):
        if 'http' in url:
            return url
        else:
            return None


def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def create_files(dir_name, base_url):
    queue_file = os.path.join(dir_name, 'queue.txt')
    crawled_file = os.path.join(dir_name, 'crawled.txt')
    if not os.path.exists(queue_file):
        write_to_file(queue_file, base_url)
    if not os.path.exists(crawled_file):
        write_to_file(crawled_file, '')


def write_to_file(file, data):
    with open(file, 'w') as f:
        f.write(data + "\n")


def append_to_file(file, data):
    with open(file, 'a') as f:
        for link in data:
            if parse_url(link):
                f.write(link + "\n")


def get_links_from_file(file):
    links = set()
    with open(file, 'r') as f:
        for link in f:
            if parse_url(link):
                links.add(link.replace("\n", ''))
    return links


def save_links_to_file(file, links):
    with open(file, 'w') as f:
        for link in links:
            if parse_url(link):
                f.write(link + "\n")
