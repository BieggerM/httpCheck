from .models import Request


class DataHandler:
    pass

    def getResponse(self, session_id, request):
        response_data = {'success': 'True', 'id': session_id, 'scheme': request.scheme, 'method': request.method,
                         'path': request.path}
        return response_data

    def saveRequest(self, session_id, request):
        request_object = Request(method=request.method, path=request.path, payload=request.body, scheme=request.scheme,
                                 id=session_id)
        request_object.save()
