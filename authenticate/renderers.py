import json


from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        token = data.get('token', None)

        if errors:
            return super(UserJSONRenderer, self).render(data)

        if token and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        if data.get('user'):
            return json.dumps(data)
        else:
            return json.dumps({'user': data})