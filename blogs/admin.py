from django.contrib import admin
from blogs.models import Blog, Category
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'data_posted')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)