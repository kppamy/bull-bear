from django import http, shortcuts
from django.contrib.auth import decorators

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

@decorators.login_required
def predict(request):
    """Handles a POST request"""
    try:
        models.Prediction.objects.create(
            user_id = request.user.id,
            outcome_id = request.POST['outcome_id'],
            staked_reputation = request.POST['staked_reputation'],
        )
    except KeyError:
        return http.HttpResponseBadRequest('Missing parameters in prediction request.')
    return http.HttpResponse("done")