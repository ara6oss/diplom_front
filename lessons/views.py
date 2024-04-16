from django.shortcuts import get_list_or_404, render

from lessons.models import Lesson, Category

# Create your views here.

# def home (request):
    
    

#     lessons = Lesson.objects.all() 
    
    
#     categories = Category.objects.all()
#     context = {
#         "lessons" : lessons,
#         "categories":categories, 
#     }
    
#     return render(request, 'home.html', context)


def home (request, category_slug='all'):
    
    
    
    if category_slug == 'all':
        lessons = Lesson.objects.all() 
    
    else:
        lessons = get_list_or_404(Lesson.objects.filter(category__slug=category_slug))
    
    categories = Category.objects.all()
    context = {
        "lessons" : lessons,
        "categories":categories,
        'slug_url' : category_slug 
    }
    
    return render(request, 'home.html', context)




def course_detail(request, course_slug):
    lesson = Lesson.objects.get(slug=course_slug)
    
    context = {
        "lesson": lesson
    }
    
    return render(request, 'lessons/playlist.html', context)