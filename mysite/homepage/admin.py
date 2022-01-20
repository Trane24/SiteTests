from django.contrib import admin
from .models import Homepage, Category


class HomepageAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "title", "datatime", "updated", "is_published")
    list_display_links = ["title"]
    search_fields = ("title", "content")
    list_aditable = ("is_published",)
    list_filter = ("is_published", "category")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ["title"]
    search_fields = ("title",)


admin.site.register(Homepage, HomepageAdmin)
admin.site.register(Category, CategoryAdmin)
