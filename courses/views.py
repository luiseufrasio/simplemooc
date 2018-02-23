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
	context = {}
	
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			print(form.cleaned_data)
			form = ContactCourse()
	else:
		form = ContactCourse()

	context['form'] = form
	context['course'] = course
	
	return render(request, 'details.html', context)