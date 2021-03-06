from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment, Announcement, Lesson, Material
from .forms import ContactCourse, CommentForm

from django.contrib import messages
from django.contrib.messages import get_messages
from .decorators import enrollment_required

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

@login_required
def undo_enrollment(request, slug):
	course = get_object_or_404(Course, slug=slug)
	enrollment = get_object_or_404(
		Enrollment, user=request.user, course=course	
	)
	if request.method == 'POST':
		enrollment.delete()
		messages.success(request, "Inscrição cancelada.")
		return redirect('accounts:dashboard')
	template = 'undo_enrollment.html'
	context = {
		'enrollment': enrollment,
		'course': course
	}
	return render(request, template, context)
	

@login_required
@enrollment_required
def announcements(request, slug):
	course = request.course
	template = 'announcements.html'
	context = {
		'course': course,
		'announcements': course.announcements.all()
	}
	return render(request, template, context)

@login_required
@enrollment_required
def show_announcement(request, slug, pk):
	course = request.course
	announcement = get_object_or_404(course.announcements.all(), pk=pk)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.user = request.user
		comment.announcement = announcement
		comment.save()
		form = CommentForm()
		messages.success(request, 'Seu comentário foi enviado com sucesso')
	template = 'show_announcement.html'
	context = {
		'course': course,
		'announcement': announcement,
		'form': form,
	}
	return render(request, template, context)

@login_required
@enrollment_required
def lessons(request, slug):
	course = request.course
	template = 'lessons.html'
	if not request.user.is_staff:
		lessons = course.release_lessons()
	else:
		lessons = course.lessons.all()
	context = {
		'course': course,
		'lessons': lessons
	}
	return render(request, template, context)
	
@login_required
@enrollment_required
def lesson(request, slug, pk):
	course = request.course
	lesson = get_object_or_404(Lesson, pk=pk, course=course)
	if not request.user.is_staff and not lesson.is_available():
		messages.error(request, 'Aula ainda não está disponível')
		return redirect('courses:lessons', slug=course.slug)
	template = 'lesson.html'
	context = {
		'course': course,
		'lesson': lesson
	}
	return render(request, template, context)

@login_required
@enrollment_required
def material(request, slug, pk):
	course = request.course
	material = get_object_or_404(Material, pk=pk, lesson__course=course)
	lesson = material.lesson
	if not request.user.is_staff and not lesson.is_available():
		messages.error(request, 'Material ainda não está disponível')
		return redirect('courses:lesson', slug=course.slug, pk=lesson.pk)
	if not material.is_embedded():
		return redirect(material.file.url)
	template = 'material.html'
	context = {
		'course': course,
		'lesson': lesson,
		'material': material,
	}
	return render(request, template, context)