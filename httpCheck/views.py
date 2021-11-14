from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from .models import Request
from .models import Session
from django.http import JsonResponse
import datetime
import random
import string


@csrf_exempt
def public_api(request):
    response_data = {'success': 'True', 'scheme': request.scheme, 'method': request.method, 'path': request.path}
    return JsonResponse(response_data)


@csrf_exempt
def public_api_with_id(request, session_id):
    if Session.objects.filter(session_id=session_id).exists():
        save_request(session_id, request)
        response_data = get_response(session_id=session_id, request=request)
        return JsonResponse(response_data)
    else:
        return JsonResponse(get_id_not_found_response(id, request))


@csrf_exempt
def public_api_with_garbage(request, session_id, garbage):
    save_request(session_id, request)
    response_data = get_response(session_id, request)
    return JsonResponse(response_data)


## Session ##
@csrf_exempt
def create_session(request):
    random_string = randStr()
    session = Session(session_id=random_string, session_start=datetime.datetime.now())
    session.save()
    return JsonResponse({"success": True, "sessionId": random_string, "path": "api/" + random_string + "/"})


## Methods ##
def get_response(session_id, request):
    response_data = {'success': 'True', 'id': session_id, 'scheme': request.scheme, 'method': request.method,
                     'path': request.path}
    return response_data


def save_request(session_id, request):
    request_object = Request(method=request.method, path=request.path, payload=request.body, scheme=request.scheme,
                             session_id=session_id)
    request_object.save()


def get_id_not_found_response(id, request):
    response_data = {'success': 'False', 'id': id, 'scheme': request.scheme, 'method': request.method,
                     'path': request.path, 'error': 'session invalid'}
    return response_data


def randStr(chars=string.ascii_uppercase + string.digits, N=15):
    while True:
        random_string = ''.join(random.choice(chars) for _ in range(N))
        if not Session.objects.filter(session_id=random_string).exists():
            return ''.join(random.choice(chars) for _ in range(N))
