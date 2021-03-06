from django import http, shortcuts
from django.contrib.auth import decorators

from . import models

def index(request):
  return shortcuts.render(request, 'bull_bear/index.html')

def events(request):
  context = {
    'latest_events': models.Event.objects.order_by('-id')[:5]
  }
  return shortcuts.render(request, 'bull_bear/events.html', context)

def profile(request, user_id):
  return shortcuts.render(request, 'bull_bear/profile.html', {})

def event(request, event_id):
  event = shortcuts.get_object_or_404(models.Event, pk=event_id)
  outcomes = [
    {
      'outcome': outcome,
      'odds': 1.0 / outcome.likelihood,
      'staked_reputation': sum([p.staked_reputation
        for p in outcome.prediction_set.filter(user_id=request.user.id)]),
      'earnable_reputation': sum([p.earnable_reputation
        for p in outcome.prediction_set.filter(user_id=request.user.id)]),
    }
    for outcome in event.outcome_set.all()
  ]
  context = {
    'user': request.user,
    'event': event,
    'outcomes': outcomes,
  }
  if request.user.is_authenticated():
    context.update({
      'thing': 'thing',
    })
  return shortcuts.render(request, 'bull_bear/event.html', context)

@decorators.login_required
def make_prediction(request):
  """Handles a POST request"""
  try:
    outcome_id = request.POST['outcome_id']
    staked_reputation = float(request.POST['reputation'])
  except KeyError:
    return http.HttpResponseBadRequest('Missing parameter in request.')

  user = request.user
  outcome = shortcuts.get_object_or_404(models.Outcome, pk=outcome_id)

  if staked_reputation > user.profile.reputation:
    return http.HttpResponseBadRequest('Staking more reputation than is available.')

  # User loses reputation.
  user.profile.reputation -= staked_reputation
  user.profile.save()

  # Configurable:
  earnable_reputation = staked_reputation / outcome.likelihood

  models.Prediction.objects.create(
    user=user,
    outcome=outcome,
    staked_reputation=staked_reputation,
    earnable_reputation=earnable_reputation,
  )
  
  # This has to happen last.
  outcome.event.update_likelihoods()

  return shortcuts.redirect(shortcuts.reverse(event, args=[outcome.event_id]))