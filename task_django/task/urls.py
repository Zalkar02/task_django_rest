from django.urls import path
from . import views as v

app_name = 'task'
urlpatterns = [
    path('', v.TaskList.as_view(), name='list'),
    path('create/', v.TaskCreate.as_view(), name='create'),
    path('<int:pk>/', v.TaskDetail.as_view(), name='detail')
]