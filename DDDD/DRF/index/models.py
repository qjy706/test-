from django.db import models

# Create your models here.
#tutorial-1-serialization

class Teachers(models.Model):
    name = models.CharField(max_length=20,verbose_name='老师')

    age = models.IntegerField(max_length=20,verbose_name='年龄')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Teachers'
        verbose_name = '老师'
        verbose_name_plural = '老师'

