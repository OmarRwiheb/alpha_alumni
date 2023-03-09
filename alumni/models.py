from django.db import models

# Create your models here.


class Alumni(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    joined_aiesec_at = models.IntegerField()
    photo = models.ImageField(
        upload_to='./alumni/alumni_images', blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
