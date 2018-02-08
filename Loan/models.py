from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
import datetime

class Advisor(AbstractUser):
    referred_by = models.BigIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', null=True, blank=True, default='avatar.jpg')
    
    def __str__(self):
        return self.first_name+' '+self.last_name

class Category(models.Model):
    name = models.CharField(u'name', max_length=250, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(u'Description', blank=True)

    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    def __str__(self):
        return self.name

    def save(self):
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super(Category, self).save()

