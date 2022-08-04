from django.conf import settings
from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    edited = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

