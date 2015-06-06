from sqlalchemy import (
    Column,
    Integer,
    Text,
    String, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Phase(Base):
    __tablename__ = 'phases'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

class GridPosition(Base):
    __tablename__ = 'grid_positions'
    position =Column(String(), primary_key=True)
    team_id = Column(Integer, ForeignKey('team.id'))


class Round(Base):
    __tablename__ = 'rounds'
    id = Column(Integer, primary_key=True)


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    team1_id = Column(Integer)
    team2_id = Column(Integer)
    winner = Column(Integer)


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text)