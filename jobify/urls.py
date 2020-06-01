from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('static.urls')),
    path('user/', include('user.urls')),
    path('jobs/', include('test_results.urls')),
    path('jobinator/', include('jobinator.urls')),
    path('webscraper/', include('webscraper.urls')),
    path('alerts/', include('alerts.urls'))
]
