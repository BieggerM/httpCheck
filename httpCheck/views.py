from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from .models import Request
from .models import Session
from django.http import JsonResponse
import datetime

# Create your views here.

@csrf_exempt
def public_api(request):
    response_data = {'success': 'True', 'scheme': request.scheme, 'method': request.method, 'path': request.path}
    return JsonResponse(response_data)


@csrf_exempt
def public_api_with_id(request, id):
    if Session.objects.filter(session_id=id).exists():
        save_request(id, request)
        response_data = get_response(id, request)
        return JsonResponse(response_data)
    else:
        return JsonResponse(get_id_not_found_response(id, request))


@csrf_exempt
def public_api_with_garbage(request, id, garbage):
    save_request(id, request)
    response_data = get_response(id, request)
    return JsonResponse(response_data)


@csrf_exempt
def create_session(request, id):
    session = Session(session_id=id, session_start=datetime.datetime.now())
    session.save()
    return JsonResponse({"success": True})


def get_response(id, request):
    response_data = {'success': 'True', 'id': id, 'scheme': request.scheme, 'method': request.method,
                     'path': request.path}
    return response_data


def save_request(id, request):
    request_object = Request(method=request.method, path=request.path, payload=request.body, scheme=request.scheme,
                             id=id)
    request_object.save()


def get_id_not_found_response(id, request):
    response_data = {'success': 'False', 'id': id, 'scheme': request.scheme, 'method': request.method,
                     'path': request.path, 'error': 'session invalid'}
    return response_data
