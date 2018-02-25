import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

class Advisor(AbstractUser):
    """ Class for saving user details"""
    referred_by = models.BigIntegerField(blank=True, null=True)
    profile_pic = models.ImageField(
        upload_to='profiles/', null=True, blank=True, default='avatar.jpg')
    contact_no = models.BigIntegerField(blank=True, null=True)
    pancard_info = models.CharField(max_length=10,blank=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    postalCode = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(blank=True, null=True)
    is_verified = models.NullBooleanField(default=False,null=True)

    class Meta:
        db_table = 'advisor'

    def __str__(self):
        return self.first_name+' '+self.last_name

class Category(models.Model):
    """ This defines the field required for category fields like loan,insurance """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=250, blank=False, null=False, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField('Description', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name

    def save(self):
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super(Category, self).save()

class Subcategory(models.Model):
    """This defines the field required for subcategory under category section """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('name', max_length=255, blank=False,null=False)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField('Description', blank=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'
        db_table = 'subcategory'

    def __str__(self):
        return self.name

    def save(self):
        date = datetime.date.today()
        self.slug = '%i/%i/%i/%s' % (
            date.year, date.month, date.day, slugify(self.name)
        )
        super(Subcategory, self).save()

class Order(models.Model):
    """ Order fields details"""

    class Meta:
        db_table = 'order'

    PRODUCT_CHOICES = (('Loan', (
            ('home loan', 'Home Loan'),
            ('loan again propery', 'LAP'),
            ('personal loan', 'Personal Loan'),
            ('car loan', 'Car Loan'),
            ('business loan', 'Business Loan'),
        )
    ),
    ('Insurance', (
            ('health insurance', 'Health Insurance'),
            ('life Insurance', 'Life Insurance'),
            ('Car Insurance','Car Insurance'),
            ('bike Insurance','Bike Insurance')
        )
    ),
    ('Other', 'Other'),)
    STATUS_CHOICES = (("pending","Pending"),("completed","Completed"),("processing","Processing"),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    referred_by = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=250,null=False,blank=False)
    contact_no = models.BigIntegerField(blank=False, null=False)
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    postalCode = models.CharField(max_length=10,blank=True,null=True,verbose_name="postal code")
    address = models.TextField(blank=True, null=True,verbose_name="Address")

    product = models.CharField(max_length=100,choices=PRODUCT_CHOICES,verbose_name='product',default="other")
    amount = models.BigIntegerField(blank=False,null=True,default=0,verbose_name='Amount')
    referal_amount = models.BigIntegerField(default=0,blank=True,null=True)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,
        default="pending")
    description = models.TextField('Description', blank=True)

