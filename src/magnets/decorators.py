import json
from functools import wraps

from flask import request, abort

from magnets.exceptions import MagnetsClientException


def magnets_route(bp, route,  *args, methods=None, dump_as_json=True, **kwargs):

    methods = methods or ['GET']

    def _decorator(func):
        @wraps(func)
        def _wrapper(**wrapper_kwargs):
            arguments = {}
            if 'POST' in methods:
                arguments.update(request.json or {})
            if 'GET' in methods:
                arguments.update(request.args or {})

            try:
                result = func(**wrapper_kwargs, **arguments)
            except MagnetsClientException as e:
                return json.dumps(str(e)), e.status_code

            return json.dumps(result) if dump_as_json else result

        return bp.route(route, methods=methods, *args, **kwargs)(_wrapper)

    return _decorator
