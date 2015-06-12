from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from kubb_match.data.models import (Base,
                                    )
from kubb_match.renderers import json_item_renderer, json_list_renderer


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.set_session_factory(SignedCookieSessionFactory(config.registry.settings['session_factory.secret']))

    # Rewrite urls with trailing slash
    config.include('pyramid_rewrite')
    config.add_rewrite_rule(r'/(?P<path>.*)/', r'/%(path)s')

    # Add jinja2
    config.include('pyramid_jinja2')

    # renderers
    config.add_renderer('listjson', json_list_renderer)
    config.add_renderer('itemjson', json_item_renderer)

    # Add SQLAlchemy
    config.include('kubb_match.data.db')

    # static views
    config.add_static_view('static', 'static', cache_max_age=3600)

    # routes
    config.add_route('home', '/')

    config.add_route('admin', '/admin')

    config.add_route('teams', '/teams')
    config.add_route('team', '/teams/{id:\d+}')

    config.add_route('rounds', '/rounds')
    config.add_route('round', '/rounds/{id:\d+}')
    config.add_route('round_games', '/rounds/{id:\d+}/games')
    config.add_route('round_game', '/rounds/{id:\d+}/games/{gid:\d+}')
    config.add_route('round_positions', '/rounds/{id:\d+}/positions')

    config.add_route('phases', '/phases')
    config.add_route('phase', '/phases/{id:\d+}')
    config.add_route('phase_status', '/phases/{id:\d+}/status')

    # HTML routes
    config.add_route('phase1', '/battle')
    config.add_route('phase1-admin', '/battle-admin')

    config.add_route('phase2', '/ko')
    config.add_route('phase2-admin', '/ko-admin')

    config.add_route('results', '/results')

    config.scan()
    return config.make_wsgi_app()
