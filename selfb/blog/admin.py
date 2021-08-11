from django.contrib import admin
from .models import Introduction,Projects,Fav,categories,HeadIntro,Sharing,comments
# Register your models here.

admin.site.register(Introduction)
admin.site.register(Projects)
admin.site.register(Fav)
admin.site.register(categories)
admin.site.register(Sharing)
admin.site.register(HeadIntro)
admin.site.register(comments)

