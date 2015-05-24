from pyramid.view import view_config


@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'title': 'Home'}


@view_config(route_name='toc', renderer='toc.pt')
def toc(request):
    return {
        'title': 'Table Of Contents',
        'toc': request.params['page_url'],
    }
