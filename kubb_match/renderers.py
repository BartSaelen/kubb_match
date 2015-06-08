# -*- coding: utf-8 -*-
from pyramid.renderers import JSON
from kubb_match.data.models import Team

json_list_renderer = JSON()
json_item_renderer = JSON()


def team_adapter(obj, request=None):
    return {
        'id': obj.id,
        'name': obj.name
    }


json_list_renderer.add_adapter(Team, team_adapter)



json_item_renderer.add_adapter(Team, team_adapter)
