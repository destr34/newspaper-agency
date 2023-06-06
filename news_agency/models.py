from django.contrib.auth.models import AbstractUser
from django.db import models

from newspaper import settings


class Topic(models.Model):
    topic = models.CharField(max_length=255)

    class Meta:
        ordering = ["topic"]

    def __str__(self) -> str:
        return self.topic


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="newspapers"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return (
            f"{self.publishers} published " 
            f"{self.title} date {self.published_date}"
        )
