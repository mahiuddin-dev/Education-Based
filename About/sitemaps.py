from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from Blog.models import Blog_Post
from Book.models import Book_Post
from Jobpost.models import Job_Post

class StaticViewSitemap(Sitemap):

    def items(self):
        return [
            'Home:home',
            'Contact:contact',
            'About:about',
            'Blog:Blog',
            'Book:book',
            'Jobpost:job',
        ]
    
    def location(self,item):
        return reverse(item)


class BlogpostSitemap(Sitemap):

    def items(self):
        return Blog_Post.objects.all()


class BoookSitemap(Sitemap):

    def items(self):
        return Book_Post.objects.all()

class JobSitemap(Sitemap):

    def items(self):
        return Job_Post.objects.all()