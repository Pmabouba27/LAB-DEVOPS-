from django.shortcuts import render
import sentry_sdk

def home(request):
    return render(request, 'portal/index.html')

def trigger_error(request):
    try:
        division_by_zero = 1 / 0  # bug simulé
    except Exception as e:
        sentry_sdk.capture_exception(e)  # envoi silencieux à Sentry
    return render(request, 'portal/index.html', {'error': True})