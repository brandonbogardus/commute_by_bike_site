from django.contrib import admin
from .models import Post, PostImage


class PostImageInline(admin.TabularInline):                         # allows posting images directly in Post admin page         
    model = PostImage                                               # associates inline with the model is represents
    extra = 1                                                       # creates one empty image field ready to go



@admin.register(Post)                                               # decorator that registers PostAdmin as the admin config for the Post model
class PostAdmin(admin.ModelAdmin):  
    list_display = ["title", "author", "date_posted"]               # controls which model fields appear in the Post aadmin
    inlines = [PostImageInline]                                     # connects PostImageInline with the PostAdmin page
