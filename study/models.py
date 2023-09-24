from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=20)

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100)
    video_link = models.CharField(max_length=200)
    video_length = models.IntegerField()
    products = models.ManyToManyField(Product)


class ViewCount(models.Model):
    """
    Модель счётчика просмотров для видео
    """
    lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    viewed_on = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    class Meta:
        ordering = ('-viewed_on',)
        indexes = [models.Index(fields=['-viewed_on'])]
        verbose_name = 'Просмотр'
        verbose_name_plural = 'Просмотры'

    def __str__(self):
        return self.lesson_name.title