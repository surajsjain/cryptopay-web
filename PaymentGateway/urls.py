from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('auth/', include('usermgmt.urls')),
]
