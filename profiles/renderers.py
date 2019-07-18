import json

from rest_framework.renderers import JSONRenderer

from .models import PassportInfo


class PassportInfoRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        if data is None:
            return json.dumps({
                'profile': 'Not found in the database'
            })
        errors = None
        if not isinstance(data, list) and data.get('errors'):
            errors = data.get('errors')
        
        if errors:
            return super(PassportInfoRenderer, self).render(data)
        if isinstance(data, list):
            return json.dumps({
                'profiles': data
            })
        else:
            return json.dumps({
                'profile': data
            })
