from django.shortcuts import render
from time import ctime
from .models import Post  # (dot).models as it's in the same directory
# from django.http import HttpResponse

# dummy data - removed

def home(request):
    contexts = {
        'posts' : Post.objects.all()  # query our DB posts just like shell (instead of dummy) - dict keys should be same as db fields
    }
    return render(request, 'fitness_programs/home.html', contexts)  # 3 arg here is context to pas info into template
    # return HttpResponse('<h1>Indifit Home</h1>')
    # views need to return http response (form of render) or an exception
    # once we pass that data in to template, then we can access it

def about(request):
    return render(request, 'fitness_programs/about.html', {'title' : 'About!!!'})  # context is short so just pass dict directly
    
