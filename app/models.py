from django.db import models

# Create your models here.
class Gift(models.Model):
    image = models.ImageField(upload_to='imgaes/')
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title