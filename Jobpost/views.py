from django.views.generic import ListView,DetailView
from .models import Job_Post
from Blog.models import Blog_Post
from django.contrib import messages
from .forms import CommentForm
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect
# Create your views here.

class JobView(ListView):
    template_name = 'job.html'
    paginate_by = 10
    queryset = Job_Post.objects.all()

class JobDetailView(DetailView):
    template_name = 'post.html'
    model = Job_Post
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_current_obj = self.get_object()

        # page view
        get_current_obj.read +=1
        get_current_obj.save(update_fields = ['read'])

        Latests = Blog_Post.objects.all().order_by('-date')[:3]

        # All approve comment
        comments = get_current_obj.comments.filter(approve=True)
        count_comment = len(comments)

        next_prv_single = Job_Post.objects.all().order_by('-date')[:2]

        if len(next_prv_single) > 0:
            context['next_prv_single'] = next_prv_single
        else:
            context['next_prv_single'] = Latests[:2]

        context['comments'] = comments
        context['count_comment'] = count_comment
        context['jobname'] = True
        context['Latests'] = Latests

        return context