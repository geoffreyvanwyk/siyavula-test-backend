from bs4 import BeautifulSoup
from pyramid.view import view_config
import urllib.request as http
import re


@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'title': 'Home'}


@view_config(route_name='table_of_contents', renderer='table_of_contents.pt')
def table_of_contents(request):
    url = request.params['page_url']
    html = http.urlopen(url).read()

    return {
        'title': 'Table Of Contents',
        'page_name': re.search(r"wiki/(.*)$", url).group(1),
        'page_url': url,
        'table_of_contents': BeautifulSoup(html).find(id="toc"),
    }
