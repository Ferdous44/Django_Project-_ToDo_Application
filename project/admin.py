from django.contrib import admin

# Register your models here.
from.models import project,Review,Tag

from.models import project
admin.site.register(project)
admin.site.register(Review)
admin.site.register(Tag)

