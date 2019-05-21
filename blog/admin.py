from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Post, Comment


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Post, MyModelAdmin)
admin.site.register(Comment)
