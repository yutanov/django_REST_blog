from django.contrib import admin
from api.models import Article, Comment
import requests

class MyModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if obj.status == 'approved':
            # Make the API call
            requests.get('http://www.example.com', params={'user': obj.userID, 'status': 'approved'})
        # Delegate the save to the parent class
        super().save_model(request, obj, form, change)

admin.site.register(Article)
admin.site.register(Comment)
