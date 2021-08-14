from web_site import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Blog)
admin.site.register(models.CodeGist)
admin.site.register(models.UserProfile)