from functools import wraps
from django.http import HttpResponseRedirect
from petition_app.models import User

def login_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        user_id = request.session.get('user')
        try:
            user = User.objects.get(id=user_id)
        except:
            user = None
        
        if user:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap