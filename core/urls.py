from django.contrib import admin
from django.urls import path
from portal.views import home, trigger_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sentry-debug/', trigger_error, name='sentry_debug'),
]