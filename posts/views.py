from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect

from .models import Article, Category
from .forms import ArticleForm
from django.utils import timezone

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
def WriteView(request):
     if request.user.is_authenticated():
         if request.method == "POST":
             form = ArticleForm(request.POST)
             if form.is_valid():
                article = form.save(commit=False)
                article.pub_date = timezone.now()
                article.save()
                return redirect('posts:detail', pk=article.pk)
         else:
             form = ArticleForm()

         return render(request, 'posts/write.html', {
            'form': form,
            'form_class': form
         })
         
      # user is not logged in      
     else:
        return HttpResponseRedirect(reverse('posts:login'))
       
#
#   CATEGORY VIEW
#       
def category(request, category_label):
    
    # 404 handler
    category = get_object_or_404(Category, category_label=category_label)
    
    # at least the 5 latest
    def get_articles_by_category(): 
        return Article.objects.filter(
            category__category_label = category_label
        )[:5]  
        
    return render(request, 'posts/category.html', {
        'articles': get_articles_by_category(),
        'category_label': category_label,
    })


class DetailView(generic.DetailView):
    model = Article
    template_name = 'posts/detail.html'
