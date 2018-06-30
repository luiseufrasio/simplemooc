from django.shortcuts import render
from django.views.generic import ListView
from .models import Thread

class ForumView(ListView):
    
    model = Thread
    paginated_by = 10
    template_name = 'index_forum.html'

index = ForumView.as_view()