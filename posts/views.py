from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect

from .models import Article, Category
from .forms import ArticleForm
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

#
#   INDEX VIEW
#
class IndexView(generic.ListView):
    template_name = 'posts/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['latest_posts_list'] = self.get_queryset()
        context['alphabetical_categories_list'] = self.get_categories()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:5]
    def get_categories(self):
        return Category.objects.order_by('id')[:5]

#
#   WRITE VIEW
#
class WriteView(LoginRequiredMixin, generic.CreateView):
    form_class = ArticleForm
    template_name = 'posts/write.html'
    login_url = '/posts/login/'


    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(WriteView, self).form_valid(form)

#
#   CATEGORY VIEW
#
class CategoryView(generic.DetailView):
    model = Category
    template_name = 'posts/category.html'

    def get_object(self):
        category_label = self.kwargs['category_label']
        return Category.objects.get(category_label=category_label)

#
#   DETAIL VIEW
#
class DetailView(generic.DetailView):
    model = Article
    template_name = 'posts/detail.html'
