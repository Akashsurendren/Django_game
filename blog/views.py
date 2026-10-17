from django.shortcuts import render


my_posts = [{
    'title': 'think like a pro',
    'content': 'I\'m a computer sciance student',
    'author' : 'John',
    'date_posted': '2/4/2025'
}
]
# Create your views here.
def home(request):
    contex ={
        'posts': my_posts
    }
    return render(request, 'blog/home.html', contex)



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})