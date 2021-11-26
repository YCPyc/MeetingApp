from django.db import models
from django.urls import reverse
# Create your models here.

# a discussion model for the post object
class Post(models.Model):
    title = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    time_duration = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True,upload_to="images/")

    class Meta:
        ordering = ['-date_added']
    # redirect to the detail page after adding a new topics
    def get_absolute_url(self):
        return reverse('frontPage')

# a discussion model for the dicussion section
class Discussion(models.Model):
    post = models.ForeignKey(Post, related_name="discussions", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']