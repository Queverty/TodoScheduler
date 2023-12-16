import json

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from users.models import User


# Create your views here.
def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    user_id = request.session.get('session_user')
    if user_id == None:
        return redirect('login')
    user = User.objects.get(id=user_id)
    return render(request, "chat/room.html",
                  {"room_name": mark_safe(json.dumps(room_name)),
                        'username':mark_safe(json.dumps(user.username))})