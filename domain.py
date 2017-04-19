
import urllib


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urllib.parse.urlparse(url).netloc
    except:
        return ''

HOMEPAGE = 'http://viper-seo.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
print DOMAIN_NAME

