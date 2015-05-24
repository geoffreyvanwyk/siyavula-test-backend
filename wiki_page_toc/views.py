from bs4 import BeautifulSoup
from pyramid.view import view_config
import urllib.request as http


@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'title': 'Home'}


@view_config(route_name='table_of_contents', renderer='table_of_contents.pt')
def table_of_contents(request):
    url = request.params['page_url']
    html = http.urlopen(url).read()
    soup = BeautifulSoup(html)

    return {
        'title': 'Table Of Contents',
        'table_of_contents': soup.find(id="toc"),
    }
