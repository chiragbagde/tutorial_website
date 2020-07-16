from django.contrib import admin
from .models import Tutorial,TutorialSeries,TutorialCategory
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.


class Tutorialadmin(admin.ModelAdmin):

    fieldsets = [
        ('Date/title' , {'fields' : ['date_published','tutorial_name']}),
        ('URL',{'fields': ['tutorial_slug']}),
        ('Series',{'fields': ['tutorial_series']}),
        ('Content', {'fields': ['tutorial_text']})
    ]

    formfield_overrides =  {
        models.TextField : {'widget' : TinyMCE()}
    }

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,Tutorialadmin)





