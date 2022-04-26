from django.db import models

class Article(models.Model):
    date_pub = models.DateTimeField(auto_now_add=True)
    title = models.CharField (max_length = 60,  blank=True, default='')
    text = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_pub']


class Comment(models.Model):
    date_pub = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply_set', null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_pub']
