import datetime

from django.shortcuts import render
from httpCheck.models import Session

def home(request):
    return render(request, "home.html", {})


def session(request):
    try:
        session_id = request.session['session_id']
    except:
        session = Session(session_start=datetime.datetime.now())
        session_id = session.rand_str()
        session.session_id = session_id
        session.save()
        request.session['session_id'] = session_id
    return render(request, "session.html", {})

def sessionreload(request):
    del request.session['session_id']
    return session(request)
