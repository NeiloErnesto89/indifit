from django.shortcuts import render
from time import ctime
# from django.http import HttpResponse

# dummy data
posts = [
    {
        'author': 'Neil',
        'title': 'blog',
        'content' : 'hello there user',
        'date' : ctime()
    },
    {
        'author': 'Andy',
        'title': 'blog2',
        'content' : 'hello there fwriend',
        'date' : ctime()
    }
]

def home(request):
    contexts = {
        'posts' : posts
    }
    return render(request, 'fitness_programs/home.html', contexts)  # 3 arg here is context to pas info into template
    # return HttpResponse('<h1>Indifit Home</h1>')
    # views need to return http response (form of render) or an exception
    # once we pass that data in to template, then we can access it

def about(request):
    return render(request, 'fitness_programs/about.html', {'title' : 'About!!!'})  # context is short so just pass dict directly
    
