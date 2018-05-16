from django.contrib import admin
from .models import Article,tags,MoringaMerch,NewsLetterRecipients

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# admin.site.register()
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)
admin.site.register(NewsLetterRecipients)
admin.site.register(MoringaMerch)
