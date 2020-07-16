from django.db import models
from datetime import datetime

# Create your models here.

class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    #for extension o url link
    category_slug = models.CharField(max_length=200, default=1)

    class Meta:
        #to avoid plural namesin admin
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_name = models.CharField(max_length=200)
    tutorial_text = models.TextField()
    tutorial_date = models.DateTimeField(name='date_published',default=datetime.now())
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_name
