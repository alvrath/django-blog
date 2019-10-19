from django.contrib import admin
from .models import Post, Category, Rubrika

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class RubrikaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register (Rubrika, RubrikaAdmin)
