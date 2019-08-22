# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from .models import Editor,Article,tags
# from .models import Product
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register( Article,ArticleAdmin)
admin.site.register(tags)
# admin.site.register(Product)
#Making Fields Optional

