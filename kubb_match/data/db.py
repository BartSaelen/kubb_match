# -*- coding: utf-8 -*-
import logging
from kubb_match.data.models import Base
from kubb_match.data.data_managers import DataManager

log = logging.getLogger(__name__)


from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension


def data_managers(request):
    session = request.db
    data_manager = DataManager(session)

    return {'data_manager': data_manager}


def db(request):
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        session.close()

    request.add_finished_callback(cleanup)

    return session


def includeme(config):
    # Setting up SQLAlchemy
    engine = engine_from_config(config.get_settings(), 'sqlalchemy.')
    Base.metadata.bind = engine
    config.registry.dbmaker = sessionmaker(
        bind=engine,
        extension=ZopeTransactionExtension()
    )
    config.add_request_method(db, reify=True)
    config.add_request_method(data_managers, reify=True)