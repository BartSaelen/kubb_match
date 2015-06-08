from pyramid.config import Configurator

from kubb_match.data.models import (Base,
                                    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # Rewrite urls with trailing slash
    config.include('pyramid_rewrite')
    config.add_rewrite_rule(r'/(?P<path>.*)/', r'/%(path)s')

    # Add jinja2
    config.include('pyramid_jinja2')

    # static views
    config.add_static_view('static', 'static', cache_max_age=3600)

    # routes
    config.add_route('home', '/')

    config.add_route('admin', '/admin')

    config.scan()
    return config.make_wsgi_app()
