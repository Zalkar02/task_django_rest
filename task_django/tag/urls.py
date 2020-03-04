from django.urls import path
from . import views as v

app_name = 'tag'
urlpatterns = [
    path('', v.TagList.as_view(), name='list'),
    path('create/', v.TagCreate.as_view(), name='create'),
    path('<int:pk>/', v.TagDetail.as_view(),name='detail')
]