from django.db import models

# Create your models here.
class Cartegory(models.Model):
    name = models.CharField(max_length = 40)


    def __str__(self):
        return self.name

    def save_Cartegory(self):
        self.save()

class Location(models.Model):

    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_Location(self):
        self.save()

class Images(models.Model):
    Images_name = models.CharField(max_length = 40)
    Images_description =models.TextField()
    Images_Cartegory = models.ForeignKey(Cartegory)
    Images_Location = models.ForeignKey(Location)

    def save_Images(self):
        self.save()
