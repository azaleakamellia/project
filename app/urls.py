from django.urls import path
from app.views import MapView

app_name = 'app'

urlpatterns = [
    path("map/", MapView.as_view()),


]



