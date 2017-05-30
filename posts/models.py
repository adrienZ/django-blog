from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.urlresolvers import reverse

@python_2_unicode_compatible  # only if you need to support Python 2
class Category(models.Model):

    # unique because used in url
    category_label = models.CharField(max_length=100, unique='True')

    def __str__(self):
        return self.category_label


@python_2_unicode_compatible  # only if you need to support Python 2
class Article(models.Model):

    article_title = models.CharField(max_length=100)
    article_text = models.CharField(max_length=900)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        # related names = use in templates avoid modify context in CategoryView
        related_name="articles"
        )

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.article_text


    # url de redirection en cas de form success
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.id})
