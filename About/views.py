from django.views.generic import TemplateView
from Blog.models import Blog_Post
from .models import About
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latestpost"] = Blog_Post.objects.all().order_by('-date')[:10]
        context["PopularPost"] = Blog_Post.objects.all().order_by('-tranding')[:10]
        context["about"] = About.objects.all()[:1]
        return context


