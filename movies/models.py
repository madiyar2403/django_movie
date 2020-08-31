from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    name = models.CharField('Имя', max_length=150)
    age = models.PositiveIntegerField('Возраст', default=0)
    image = models.ImageField('Фото', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'

class Genre(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'