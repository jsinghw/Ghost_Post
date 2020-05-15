from django.db import models
from django.utils import timezone

# Create your models here.

BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))


class Post(models.Model):
    is_boast = models.BooleanField()
    content = models.CharField(max_length=280)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content
