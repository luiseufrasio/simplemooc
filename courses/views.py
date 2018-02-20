from django.shortcuts import render
from .models import Course
from .forms import ContactCourse

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

	if request.method == 'POST':
		form = ContactCourse(request.POST)
	else:
		form = ContactCourse()

	return render(request, 'details.html', {
		'course': course,
		'form': form
	})