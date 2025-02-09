from django.urls import path
from .views import HomePageView

#
# need to develop patterns and then uncomment settings.py, urls.py in trip_planner app
#
urlpatterns = [
    path("", HomePageView.as_view(), name="home")
]