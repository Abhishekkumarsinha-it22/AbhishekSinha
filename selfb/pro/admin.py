from django.contrib import admin
from .models import Blogpost,categories

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(categories)
