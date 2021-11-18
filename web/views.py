import datetime

from django.shortcuts import render
from httpCheck.models import Session
from httpCheck.models import Request


def home(request):
    return render(request, "home.html", {})


def session(request):
    try:
        session_id = request.session['session_id']
    except:
        session_object = Session(session_start=datetime.datetime.now())
        session_object.session_id = session_object.rand_str()
        session_object.save()
        request.session['session_id'] = session_id

    request_objects = Request.objects.filter(session_id=session_id)

    return render(request, "session.html", {'request_objects': request_objects})


def sessionreload(request):
    del request.session['session_id']
    return session(request)
