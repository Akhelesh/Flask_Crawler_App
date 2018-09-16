import os
import tldextract
from flask import current_app


def get_links(domain_name):
    path = os.path.join('data', domain_name)
    crawled_links = []
    external_links = []
    print(path)
    with open(path + '/crawled.txt', 'r') as f:
        for l in f:
            if l:
                crawled_links.append(l)

    with open(path + '/external.txt', 'r') as f:
        for l in f:
            if l:
                external_links.append(l)

    return crawled_links, external_links


def get_unique_domains(links):
    unique_domains = dict()
    for l in links:
        domain = tldextract.extract(l)
        if domain not in unique_domains:
            unique_domains[domain.domain] = 'http://' + domain.subdomain\
                + '.' + domain.domain + '.' + domain.suffix
    return unique_domains
