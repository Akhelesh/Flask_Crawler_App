import tldextract
from pycrawler.models import Domain


def get_links(domain_name):
    domain = Domain.query.filter_by(domain_name=domain_name).first()
    return (domain.internal_links.split('\n'),
            domain.external_links.split('\n'))


def get_unique_domains(links):
    unique_domains = dict()
    for l in links:
        domain = tldextract.extract(l)
        domain_name = domain.domain
        subdomain = domain.subdomain
        suffix = domain.suffix
        if domain_name not in unique_domains:
            unique_domains[domain_name] = 'http://'
            if subdomain:
                unique_domains[domain.domain] += domain.subdomain + '.'
            unique_domains[domain_name] += domain_name + '.' + suffix

    return unique_domains
