from django.apps import AppConfig
from django.contrib import admin
from news.models import Article

admin.site.register(Article)


class NewsConfig(AppConfig):
    name = 'news'
