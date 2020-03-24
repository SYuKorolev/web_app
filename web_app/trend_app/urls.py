from django.urls import path

from .api.views import DescView

app_name = "trend_app"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('description/', DescView.as_view()),
    #path('^description/(?P<name>.+)/$', DescView.as_view()),
]