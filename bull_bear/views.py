from django import http, shortcuts

def index(request):
    return shortcuts.render(request, 'bull_bear/index.html', {})

def user(request, user_id):
	return http.HttpResponse(user_id)

def gamble(request, gamble_id):
	return http.HttpResponse(gamble_id)
