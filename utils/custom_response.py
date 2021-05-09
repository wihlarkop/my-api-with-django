from django.http import JsonResponse as response_json


def JsonResponse(data, meta=None, messages=None, code=200):
    if meta is None:
        meta = {}

    if messages is None:
        messages = 'Success'

    result = {
        'data': data,
        'meta': meta,
        'message': messages,
        'code': code
    }

    return response_json(result)
