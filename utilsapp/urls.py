
from django.urls import path
from utilsapp.views import MapView

app_name = 'utilsapp'

urlpatterns = [
    path("map/", MapView.as_view()),

]

