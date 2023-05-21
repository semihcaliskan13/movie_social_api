from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Quote(models.Model):
    movie_id = models.CharField(max_length=30, null=True)
    movie_name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=500,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'quote'
        managed = True
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
            return self.movie_name + " " + self.description
