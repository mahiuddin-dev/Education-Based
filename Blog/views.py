from django.views.generic import ListView,DetailView
from .models import Blog_Post,Category_List
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from django.contrib import messages
from datetime import datetime,timedelta
from dateutil import tz
# Create your views here.

class BlogView(ListView):
    template_name = 'trending.html'
    paginate_by = 10
    queryset = Blog_Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['name'] = 'All Post'
        return context

class CategoryView2(ListView):
    template_name = "trending.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return Blog_Post.objects.filter(category=self.kwargs.get("slug"))
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Category_List.objects.get(pk=self.kwargs.get("slug"))
        return context

class BlogDetailView(DetailView):
    template_name = 'post.html'
    model = Blog_Post
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
         comment_form = CommentForm(request.POST)
         if comment_form.is_valid():
             new_comment = comment_form.save(commit=False)    
             new_comment.post= self.get_object()            
             new_comment.save() 

             messages.success(request, 'Your comment submitted. Please wait for approve.')

             context = {"messages":True}
             return HttpResponseRedirect(request.path_info,context)
         else:       
            comment_form = CommentForm()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        get_current_obj = self.get_object()
        # page view
        get_current_obj.read +=1
        get_current_obj.save(update_fields = ['read'])

        utc = tz.tzutc()
        local = tz.tzlocal()
        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=utc)
        local_now = utc_now.astimezone(local)

        date = get_current_obj.tranding_date
        check_tranding = date+ timedelta(days=7)

        if local_now > check_tranding:
            get_current_obj.tranding = 0
            get_current_obj.tranding_date = local_now
            get_current_obj.save(update_fields = ['tranding'])
            get_current_obj.save(update_fields = ['tranding_date'])
        else:
            get_current_obj.tranding +=1
            get_current_obj.save(update_fields = ['tranding'])


        
        # All approve comment
        comments = get_current_obj.comments.filter(approve=True)
        count_comment = len(comments)
        context['comments'] = comments
        context['count_comment'] = count_comment

        Latests = Blog_Post.objects.all().order_by('-date').exclude(pk=get_current_obj.pk)[:3]

        next_prv_single = Blog_Post.objects.filter(category=get_current_obj.category).order_by('-date').exclude(pk=get_current_obj.pk)[:2]

        if len(next_prv_single) > 0:
            context['next_prv_single'] = next_prv_single
        else:
            context['next_prv_single'] = Latests[:2]

        context['Latests'] = Latests

        return context

def new(request):
    return render(request,'new.html')


def CategoryView(request,slug):
    category_post = Blog_Post.objects.filter(category=slug)
    # category name
    category_name = Category_List.objects.get(pk=slug)

    context = {'page_obj': category_post,'name' : category_name}
    
    return render(request,'trending.html',context)
   

def BlogDetails(request,slug):

    try:
        post = Blog_Post.objects.get(slug=slug)
        comments = post.comments.filter(approve=True)

        if request.method == 'POST':      
            comment_form = CommentForm(request.POST)    
            if comment_form.is_valid():       
                new_comment = comment_form.save(commit=False)          
                new_comment.post = post            
                new_comment.save()
                # redirect to a new URL:           
                messages.success(request, 'Your comment submitted. Please wait for approve.')

                return HttpResponseRedirect(request.path_info)
        else:       
            comment_form = CommentForm()
    
    
        context = {'post': post, 'comments': comments}

        return render(request, 'post.html', context)
    except Exception:
        return render(request,'404.html')
