from django.contrib import admin

from articles.models import Article, Section

# Register your models here.
admin.site.register([Article, Section])