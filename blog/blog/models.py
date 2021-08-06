# Import modules
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create custom manager
class ArticlesManager(models.Manager):
    def published_articles(self):
        return self.filter(status='p')

# Create Category model
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='زیردسته', related_name='children')
    title = models.CharField(max_length=64, verbose_name="عنوان دسته بندی")
    description = models.TextField(
        max_length=200, verbose_name="توضیحات دسته بندی")
    slug = models.SlugField(max_length=128, unique=True,
                            verbose_name="آدرس دسته بندی")
    thumbnail = models.ImageField(
        upload_to='images', verbose_name="تصویر دسته بندی")
    status = models.BooleanField(verbose_name="نمایش داده شود")
    position = models.IntegerField(verbose_name='موقعیت دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title


# Create Article model
class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
    )
    title = models.CharField(max_length=64, verbose_name="عنوان")
    description = models.TextField(verbose_name="محتوا")
    slug = models.SlugField(max_length=128, unique=True,
                            verbose_name="آدرس مقاله")
    thumbnail = models.ImageField(
        upload_to='images', verbose_name="تصویر مقاله")
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="تاریخ و زمان منتشر شدن")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,
                              verbose_name="منتشر شدن / ذخیره در پیش نویس ها")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticlesManager()
    


#Create About us model
class About(models.Model):
    name = models.CharField(max_length=128, verbose_name='نام')
    phone_number = PhoneNumberField(verbose_name='شماره تلفن')
    description = models.TextField(max_length=512, verbose_name='توضیحات')
    address = models.CharField(max_length=256, verbose_name='آدرس')
    email = models.EmailField(max_length=256, verbose_name='ایمیل')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.name
