"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import tmpl_context as c
from pylons.controllers import WSGIController
from pylons.i18n import _, ungettext, N_

from tw.mods.pylonshf import render, render_response, validate

import bluechips.lib.helpers as h
from bluechips import model
from bluechips.model import meta

from paste.request import construct_url
from paste.httpexceptions import HTTPMovedPermanently

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        if environ['pylons.routes_dict']['controller'] != 'error':
            if environ['PATH_INFO'].endswith('/index'):
                environ['PATH_INFO'] = environ['PATH_INFO'][:-5]
                raise HTTPMovedPermanently(construct_url(environ))
            if not environ['PATH_INFO'].endswith('/') and \
                    environ['pylons.routes_dict']['action'] is 'index':
                environ['PATH_INFO'] += '/'
                raise HTTPMovedPermanently(construct_url(environ))
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()

__all__ = ['c', 'h', 'render', 'render_response', 'validate',
           'model', 'meta', '_', 'ungettext', 'N_', 'BaseController']