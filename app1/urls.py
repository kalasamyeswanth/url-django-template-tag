from django.urls import path
from . import views

app_name = 'ss'
urlpatterns = [
    path('link1/',views.link1,name = 'link1'),
    path('link2/',views.link2,name = 'link2'),
]