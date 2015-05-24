from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    config.add_route('home', '/')
    config.add_route('table_of_contents', '/table_of_contents')
    config.scan('.views')

    return config.make_wsgi_app()