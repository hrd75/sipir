from django.contrib import admin

# Register your models here.
from .models import PostData, PostUser, PostRuangan, PostSatker

admin.site.register(PostData)
admin.site.register(PostUser)
admin.site.register(PostRuangan)
admin.site.register(PostSatker)
    
