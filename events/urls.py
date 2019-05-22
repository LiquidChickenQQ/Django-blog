from django.urls import path
from .views import *
from . import models

urlpatterns = [
    path('', PostListView.as_view(), name='events-home'),
    path('past', PreviousEvents.as_view(), name='past-events')
]
