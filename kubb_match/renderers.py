# -*- coding: utf-8 -*-
from pyramid.renderers import JSON
from kubb_match.data.models import Team, Round, Game, KOPosition, GridPosition, Phase

json_list_renderer = JSON()
json_item_renderer = JSON()


def team_adapter(obj, request=None):
    return {
        'id': obj.id,
        'name': obj.name
    }


def round_list_adapter(obj, request=None):
    return {
        'id': obj.id,
        'final': obj.final,
        'played': obj.played
    }


def round_item_adapter(obj, request=None):
    return {
        'id': obj.id,
        'final': obj.final,
        'played': obj.played,
        'phase_id': obj.phase_id
    }


def game_adapter(obj, request=None):
    return {
        'id': obj.id,
        'team1_id': obj.team1_id,
        'team2_id': obj.team2_id,
        'round_id': obj.round_id,
        'winner': obj.winner
    }


def grid_position_adapter(obj, request=None):
    return {
        'id': obj.id,
        'round_id': obj.round_id,
        'team_id': obj.team_id,
        'type': obj.type,
        'position': obj.position
    }


def ko_position_adapter(obj, request=None):
    return {
        'id': obj.id,
        'round_id': obj.round_id,
        'team_id': obj.team_id,
        'type': obj.type,
        'same_position': obj.same_position,
        'position': obj.position
    }


def phase_item_adapter(obj, request=None):
    return {
        'id': obj.id,
        'type': obj.type,
        'rounds': obj.rounds
    }


def phase_list_adapter(obj, request=None):
    return {
        'id': obj.id,
        'type': obj.type
    }


json_list_renderer.add_adapter(Team, team_adapter)
json_list_renderer.add_adapter(Round, round_list_adapter)
json_list_renderer.add_adapter(Game, game_adapter)
json_list_renderer.add_adapter(GridPosition, grid_position_adapter)
json_list_renderer.add_adapter(KOPosition, ko_position_adapter)
json_list_renderer.add_adapter(Phase, phase_list_adapter)

json_item_renderer.add_adapter(Team, team_adapter)
json_item_renderer.add_adapter(Round, round_item_adapter)
json_item_renderer.add_adapter(Game, game_adapter)
json_item_renderer.add_adapter(GridPosition, grid_position_adapter)
json_item_renderer.add_adapter(KOPosition, ko_position_adapter)
json_item_renderer.add_adapter(Phase, phase_item_adapter)
