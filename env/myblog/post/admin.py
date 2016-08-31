from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','updated', 'timestamp')
    list_display_links = [ 'title','updated', 'timestamp']
    #filter_vertical = ['title', 'updated']
    list_filter = ['updated', 'timestamp']
    list_editable = []
    save_on_top = True
    search_fields  = ['title']

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
