from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as mediaserve
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from About.sitemaps import StaticViewSitemap,BlogpostSitemap,BoookSitemap,JobSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'blogpost':BlogpostSitemap,
    'Projects':BoookSitemap,
    'services':JobSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls', namespace='Home')),
    path('blog/', include('Blog.urls', namespace='Blog')),
    path('jobs/', include('Jobpost.urls', namespace='Jobpost')),
    path('book/', include('Book.urls', namespace='Book')),
    path('about/', include('About.urls', namespace='About')),
    path('contact/', include('Contact.urls', namespace='Contact')),
    path("robots.txt", TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path("sitemap.xml", sitemap, {'sitemaps':sitemaps}, 
    name='django.contrib.sitemaps.views import sitemap'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
        mediaserve,
        {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()