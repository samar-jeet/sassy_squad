from django.db import models

class Memory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='memory_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    drive_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
