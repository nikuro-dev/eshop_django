from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

    

class ProductCategory(models.Model):
    title = models.CharField(max_length=300 , verbose_name='عنوان', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url', db_index=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')
    def __str__(self):
        return f"{self.title} - {self.url_title}"
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class ProductBrand(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField()
    
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'تمامی برندها'   

    def __str__(self) -> str:
        return self.title
    
    
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    slug = models.SlugField(default="", null=False, db_index=True,blank=True, unique=True,verbose_name='عنوان در url')
    brand = models.ForeignKey(ProductBrand, on_delete= models.CASCADE, verbose_name='برند')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.CharField(max_length=360, null=True, db_index=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(null=False, db_index=True, verbose_name='توضیحات اصلی')
    is_active = models.BooleanField(default=False , verbose_name='فعال/غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده')
    
    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
    
    def __str__(self) -> str:
        return f"{self.title} ({self.price})"
    
    def save(self,*args, **kwargs) :
        #self.slug = slugify(self.title) 
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'تمامی محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=200, verbose_name='عنوان تگ', db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_tags')
    
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'
    
    def __str__(self):
        return self.caption