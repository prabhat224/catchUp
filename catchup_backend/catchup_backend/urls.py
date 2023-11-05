from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('api/', include('friends.urls')),
    path('api/travel/', include('travel.urls')),
    path('api/common-dates/', include('commondate.urls')),
]
