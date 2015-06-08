# -*- coding: utf-8 -*-



def map_team(team_json, team):
    team.name = team_json.get('name', None)
    return team
