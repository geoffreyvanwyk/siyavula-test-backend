from bs4 import BeautifulSoup
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest
import urllib.request as http
from .lib import (validate_url, get_page_name)


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {}


@view_config(route_name='table_of_contents', renderer='templates/table_of_contents.jinja2')
def table_of_contents(request):
    url = validate_url(request.params['page_url'])
    html = http.urlopen(url).read()

    return {
        'title': 'Table Of Contents',
        'page_name': get_page_name(url),
        'page_url': url,
        'table_of_contents':
            BeautifulSoup(html).find(id="toc") or
            'The page does not have a table of contents.',
    }


@view_config(context=HTTPBadRequest, renderer='templates/home.jinja2')
def validation_failure(exception, request):
    return {'detail': exception.detail}
