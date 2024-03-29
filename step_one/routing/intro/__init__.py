#!usr/bin/env python3

from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('home', '/howdy/{first}/{last}')
    config.add_route('homeh', '/howdyh')
    config.scan('.views')
    return config.make_wsgi_app()
