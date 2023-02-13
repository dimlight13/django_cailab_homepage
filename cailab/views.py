from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Biography, Projects, News, NewsImage
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .utils import *
from hitcount.views import HitCountDetailView

# Create your views here.


def index(req):
    return render(req, "index.html")


def publications(req):
    pub_list = preprocessing_journal_data()
    kci_list = preprocessing_korean_journal_data()
    context = {'data': pub_list, 'kci_data': kci_list}
    return render(req, "publications.html", context=context)


def professor(req):
    return render(req, "professor.html")


def applications(req):
    return render(req, "applications.html")


def student(req):
    biographies = Biography.objects.all()
    return render(req, "student.html", {'biographies': biographies})


def projects(req):
    projects = Projects.objects.all()
    proj_list = preprocessing_completed_project_data()
    context = {'projects': projects, 'completed_projects': proj_list}
    return render(req, "projects.html", context)


def area(req):
    return render(req, "area.html")


def news(req):
    news = News.objects.all()
    photos = NewsImage.objects.all()
    return render(req, "news.html", {'news': news, 'photos': photos})


def alumni(req):
    return render(req, "alumni.html")


def library(req):
    post_list = Post.objects.order_by('-createDate')
    paginator = Paginator(post_list, 10)
    page = req.GET.get('page')
    posts = paginator.get_page(page)
    return render(req, "library.html", {'posts': posts})


def seminar(req):
    return render(req, "seminar.html")


class BiographyDetailView(DetailView):
    model = Biography


class ProjectDetailView(DetailView):
    model = Projects


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    template = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        temp = Post.objects.order_by('-createDate')
        paginator = Paginator(temp, 10)
        page = self.request.GET.get('page')
        posts = paginator.get_page(page)
        context['post_list'] = posts
        return context
