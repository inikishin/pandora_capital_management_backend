from django.contrib import admin
from .models import Tag, Source, News

admin.site.register(Tag)
admin.site.register(Source)
admin.site.register(News)
