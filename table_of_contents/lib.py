from pyramid.httpexceptions import HTTPBadRequest
from urllib.parse import urlparse
import re


def validate_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url[1]
    path = parsed_url[2]

    if not re.match(r".*wikipedia.org", domain):
        raise HTTPBadRequest(detail='The URL does not contain a Wikipedia domain.')

    if not re.match(r"/wiki/[a-zA-Z0-9_]+$", path):
        raise HTTPBadRequest(detail='The path to the page is not correct.')

    return url


def get_page_name(url):
    path = urlparse(url)[2]
    return path.split('/')[-1]
