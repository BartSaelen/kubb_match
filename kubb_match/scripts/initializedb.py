import os
import sys

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from pyramid.scripts.common import parse_vars
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
import transaction
from zope.sqlalchemy import ZopeTransactionExtension

from kubb_match.data.models import (
    Base,
    Team, Phase)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_maker = sessionmaker(
        bind=engine,
        extension=ZopeTransactionExtension()
    )
    db_session = session_maker()
    with transaction.manager:
        phase = Phase()
        phase.id = 1
        phase.type = 'battle'
        db_session.add(phase)

        phase = Phase()
        phase.id = 2
        phase.type = 'ko'
        db_session.add(phase)

        team = Team()
        team.name = 'Pirates of the kubbibian'
        db_session.add(team)

        team = Team()
        team.name = 'Kubb met Appelmoes'
        db_session.add(team)

        team = Team()
        team.name = 'Das Kubb'
        db_session.add(team)

        team = Team()
        team.name = 'Klimop'
        db_session.add(team)

        team = Team()
        team.name = 'De Dissers'
        db_session.add(team)

        team = Team()
        team.name = 'BVBA Van Roosbroeck'
        db_session.add(team)

        team = Team()
        team.name = 'The Kubboys'
        db_session.add(team)

        team = Team()
        team.name = 'Kaatjes Kubbmaten'
        db_session.add(team)

        team = Team()
        team.name = 'NE KUBB BETON'
        db_session.add(team)

        team = Team()
        team.name = 'Oude Ketel'
        db_session.add(team)

        team = Team()
        team.name = 'De Ronny\'s'
        db_session.add(team)

        team = Team()
        team.name = 'Kubbpiler - Mannen Weten Waarom'
        db_session.add(team)

        team = Team()
        team.name = 'de Kubbvaders'
        db_session.add(team)

        team = Team()
        team.name = 'the Ladies'
        db_session.add(team)

        team = Team()
        team.name = 'Team Awesome'
        db_session.add(team)

        team = Team()
        team.name = 'Ge zijt zelf een kubbploeg'
        db_session.add(team)

        team = Team()
        team.name = 'Toemetoch'
        db_session.add(team)

        team = Team()
        team.name = 'The Pink Panthers 1'
        db_session.add(team)

        team = Team()
        team.name = 'The Pink Panthers 2'
        db_session.add(team)

        team = Team()
        team.name = 'Woodstock'
        db_session.add(team)

        team = Team()
        team.name = 'Landelijke Gilde Heist'
        db_session.add(team)

        team = Team()
        team.name = 'Kubbaholics'
        db_session.add(team)

        team = Team()
        team.name = 'The pink pussies'
        db_session.add(team)

        team = Team()
        team.name = 'Ploeg G'
        db_session.add(team)

        team = Team()
        team.name = 'OLHAM'
        db_session.add(team)

        team = Team()
        team.name = 'Haldisse'
        db_session.add(team)

        team = Team()
        team.name = 'Kubb Monsieur'
        db_session.add(team)

        team = Team()
        team.name = '[EZR]Kubbmaten'
        db_session.add(team)

        team = Team()
        team.name = 'upperkubb'
        db_session.add(team)

        team = Team()
        team.name = 'Cafe den hoek'
        db_session.add(team)

        team = Team()
        team.name = 'de Berthoutkubbers'
        db_session.add(team)

        team = Team()
        team.name = 'De Chouffkes'
        db_session.add(team)

        team = Team()
        team.name = '2 girls and a Kubb'
        db_session.add(team)

        team = Team()
        team.name = 'Woordspelingen zijn voor losers!'
        db_session.add(team)

        team = Team()
        team.name = 'De hete Marjetten'
        db_session.add(team)

        team = Team()
        team.name = 'Lucky Players'
        db_session.add(team)

        team = Team()
        team.name = '40+ nen disser'
        db_session.add(team)

        team = Team()
        team.name = 'De leiding van\'t Centrum '
        db_session.add(team)

        team = Team()
        team.name = 'De Mirakelkubbers'
        db_session.add(team)

        team = Team()
        team.name = 'Pleinies'
        db_session.add(team)

