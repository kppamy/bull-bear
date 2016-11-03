from django import http, shortcuts

from . import models

def index(request):
    context = {
        'latest_events': models.Event.objects.order_by('-id')[:5]
    }
    return shortcuts.render(request, 'bull_bear/index.html', context)

def user(request, user_id):
    return shortcuts.render(request, 'bull_bear/user.html', {})

def event(request, event_id):
	return http.HttpResponse(event_id)
