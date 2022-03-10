from .models import Category_List, Blog_Post
from Jobpost.models import Job_Post

def Category(request):
    try:
        category = Category_List.objects.all().order_by('name')
        return {'category':category}
    except Exception:
        category = ''
        return {'category':category}

def BlogPost(request):
    try:
        Latest = Blog_Post.objects.all().order_by('-date')[:5]
        Popular = Blog_Post.objects.all().order_by('-read')[:5]
        Tranding = Blog_Post.objects.all().order_by('-tranding')[:5]
        Jobpost = Job_Post.objects.all().order_by('-date')[:5]
        return {'Latest':Latest, 'Popular':Popular, 'Tranding':Tranding, 'Jobpost':Jobpost}
    except Exception:
        Latest = ''
        Popular = ''
        Tranding = ''
        return {'Latest':Latest, 'Popular':Popular, 'Tranding':Tranding}

