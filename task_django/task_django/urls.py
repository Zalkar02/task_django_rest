from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tags/', include('tag.urls')),
    path('api/tasks/', include('task.urls'))
]
