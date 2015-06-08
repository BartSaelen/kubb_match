from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    Text,
    String, ForeignKey)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    relationship)
from sqlalchemy.orm.collections import attribute_mapped_collection

Base = declarative_base()


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'position',
        'polymorphic_on': type
    }


class GridPosition(Position):
    __tablename__ = 'grid_positions'
    id = Column(Integer, ForeignKey('positions.id'), primary_key=True, autoincrement=True)
    position = Column(String())

    __mapper_args__ = {
        'polymorphic_identity': 'grid_position',
    }


class KOPosition(Position):
    __tablename__ = 'ko_positions'
    id = Column(Integer, ForeignKey('positions.id'), primary_key=True, autoincrement=True)
    same_position = Column(Integer)
    position = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'ko_position',
    }


class Round(Base):
    __tablename__ = 'rounds'
    id = Column(Integer, primary_key=True, autoincrement=True)
    final = Column(Boolean())
    games = relationship("Game")
    positions = relationship("Position")


class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, autoincrement=True)
    team1_id = Column(Integer, ForeignKey('teams.id'))
    team2_id = Column(Integer, ForeignKey('teams.id'))
    round_id = Column(Integer, ForeignKey('rounds.id'))
    winner = Column(Integer)


class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
