from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from .models import Request
from django.http import JsonResponse


# Create your views here.

@csrf_exempt
def public_api(request):
    response_data = {'success': 'True', 'scheme': request.scheme, 'method': request.method, 'path': request.path}
    return JsonResponse(response_data)


@csrf_exempt
def public_api_with_id(request, id):
    saveRequest(id, request)
    response_data = getResponse(id, request)
    return JsonResponse(response_data)


@csrf_exempt
def public_api_with_garbage(request, id, garbage):
    saveRequest(id, request)
    response_data = getResponse(id, request)
    return JsonResponse(response_data)


def getResponse(id, request):
    response_data = {'success': 'True', 'id': id, 'scheme': request.scheme, 'method': request.method, 'path': request.path}
    return response_data


def saveRequest(id, request):
    request_object = Request(method=request.method, path=request.path, payload=request.body, scheme=request.scheme, id=id)
    request_object.save()
