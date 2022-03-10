from unicodedata import category
from django.views.generic import TemplateView
from Blog.models import Blog_Post
from itertools import chain

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'


    def SliteData(self,slider,object,limit,filter_by_model):
        if  len(slider) < limit:
            need_limit = limit - len(slider)
            model_obj = object.objects.all().order_by(filter_by_model)[:need_limit]
            now_slider = list(chain(slider, model_obj))
            return now_slider
        else:
            now_slider = slider
            return now_slider
  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        home_slider = Blog_Post.objects.filter(home_slider=True).order_by('-home_slider')[:10]
        feature_news = Blog_Post.objects.filter(feature_news=True).order_by('-feature_news')[:10]
 
        context['home_slider'] = self.SliteData(home_slider,Blog_Post,10,'-tranding')
        context['feature_news'] = self.SliteData(feature_news,Blog_Post,10,'-tranding')
        
        # 7 post
        context['blogs'] = Blog_Post.objects.all().order_by('title')[:7]
        return context
    
