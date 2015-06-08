# -*- coding: utf-8 -*-
from pyramid.view import view_defaults, view_config


@view_defaults(request_method='GET', accept='text/html')
class HtmlView(object):
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.jinja2')
    def home(self):

        return {}

    @view_config(route_name='admin', renderer='admin.jinja2', permission='admin')
    def home(self):

        return {}
