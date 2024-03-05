from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='shop/', null=True, blank=True, verbose_name='изображение')
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name='slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    title = models.CharField(max_length=50, verbose_name='название')
    image = models.ImageField(upload_to='shop/', null=True, blank=True, verbose_name='изображение')
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name='slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    title = models.CharField(max_length=100, verbose_name='название')
    image = models.ImageField(upload_to='shop/', null=True, blank=True, verbose_name='изображение')
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name='slug')
    price = models.IntegerField(null=True, blank=True, verbose_name='цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
