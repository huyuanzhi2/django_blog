from django.contrib import admin
from blog.models import *
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','created')
admin.site.register(Blog,BlogPostAdmin)
admin.site.register(Catagory)
admin.site.register(Tag)
admin.site.register(Comment)