from django.shortcuts import render, get_object_or_404

from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    course = get_object_or_404(Course, pk=pk) #This line adds a 404 error if no objetcs are available instead of standard django 505 error like above
    return render (request, 'courses/course_detail.html', {'course': course})
