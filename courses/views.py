from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    
    context = {
        'courses': courses
    }
    
    return render(request, 'index.html', context)

# def details(request, pk):
# 	course = Course.objects.get(pk=pk)

# 	return render(request, 'details.html', {
# 		'course': course
# 	})
	
def details(request, slug):
	course = Course.objects.get(slug=slug)

	return render(request, 'details.html', {
		'course': course
	})