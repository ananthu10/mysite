from django.contrib import admin
from myapp.models import Topic, Webpage, AccessRecord
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
# Register your models here.
