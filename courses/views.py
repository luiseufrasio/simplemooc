from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment
from .forms import ContactCourse

from django.contrib import messages
from django.contrib.messages import get_messages

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
	course = get_object_or_404(Course, slug=slug)
	context = {}
	
	if request.method == 'POST':
		form = ContactCourse(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			print(form.cleaned_data)
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()

	context['form'] = form
	context['course'] = course
	
	return render(request, 'details.html', context)

@login_required
def enrollment(request, slug):
	course = get_object_or_404(Course, slug=slug)
	enrollment, created = Enrollment.objects.get_or_create(
		user = request.user, course=course
	)
	if created:
		messages.success(request, 'Você foi inscrito no curso com sucesso')
	else:
		messages.info(request, 'Você já está inscrito neste curso')

	return redirect('accounts:dashboard')