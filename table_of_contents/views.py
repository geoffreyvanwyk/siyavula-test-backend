from bs4 import BeautifulSoup
from pyramid.view import view_config
import urllib.request as http
from .lib import (validate_url, get_page_name)


@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    return {'title': 'Home'}


@view_config(route_name='table_of_contents', renderer='table_of_contents.jinja2')
def table_of_contents(request):
    url = validate_url(request.params['page_url'])
    html = http.urlopen(url).read()

    return {
        'title': 'Table Of Contents',
        'page_name': get_page_name(url),
        'page_url': url,
        'table_of_contents': BeautifulSoup(html).find(id="toc"),
    }
