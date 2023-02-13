from django.contrib import admin
from cailab.models import Biography, Post, Projects, News, NewsImage

# Register your models here.
admin.site.register(Post)
admin.site.register(Biography)
admin.site.register(Projects)
# admin.site.register(News)


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]

    class Meta:
        model = News


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    pass
