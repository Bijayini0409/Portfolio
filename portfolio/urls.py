
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('profile_page/', include('profile_page.urls')),
    path('project/', include('projects.urls')),
    path('contact/', include('contact.urls'))

]
