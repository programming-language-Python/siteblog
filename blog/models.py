from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    # автоматическое формирование ссылок
    def get_absolute_url(self):
        # 1 аргумент название маршрута
        # 2 аргумент словарь, где ключ это тот аргумент, который мы ожидаем
        # self.slug: self - текущий объект; slug - атрибут
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    # автоматическое формирование ссылок
    def get_absolute_url(self):
        # 1 аргумент название маршрута
        # 2 аргумент словарь, где ключ это тот аргумент, который мы ожидаем
        # self.slug: self - текущий объект; slug - атрибут
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    # если модель объявлена после то заносим её в кавычки
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    # автоматическое формирование ссылок
    def get_absolute_url(self):
        # 1 аргумент название маршрута
        # 2 аргумент словарь, где ключ это тот аргумент, который мы ожидаем
        # self.slug: self - текущий объект; slug - атрибут
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
