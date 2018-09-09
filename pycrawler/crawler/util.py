import os


# def parse_url(url):
#         if 'http' in url:
#             return url.split('#')[0]
#         else:
#             return None


def create_dir(dir_name):
    path = os.path.join('data', dir_name)
    if not os.path.exists(path):
        os.makedirs(path)


def create_files(dir_name, base_url):
    queue_file = os.path.join('data', dir_name, 'queue.txt')
    crawled_file = os.path.join('data', dir_name, 'crawled.txt')
    external_file = os.path.join('data', dir_name, 'external.txt')
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
    path = os.path.join('data', file)
    with open(path, 'r') as f:
        for link in f:
            if link:
                links.add(link.replace("\n", ''))
    return links


def save_links_to_file(file, links):
    path = os.path.join('data', file)
    with open(path, 'w') as f:
        for link in links:
            if link:
                f.write(link + "\n")
