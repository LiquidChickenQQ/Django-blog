from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Event, Pictures

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  )


class PostListView(ListView):
    model = Event
    template_name = 'event/events_landing.html'
    context_object_name = 'events'
    ordering = ['-date_posted']
    paginate_by = 4


class PreviousEvents(ListView):
    model = Pictures
    template_name = 'event/past_events.html'
    context_object_name = 'pics'
    ordering = ['-date_posted']
    paginate_by = 25
