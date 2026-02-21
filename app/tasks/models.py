from django.db import models
from django.utils import timezone
from projects.models import Project

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    priority = models.PositiveSmallIntegerField(
        choices=PRIORITY_CHOICES,
        default=2
    )
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-priority', 'deadline']  # сначала высокие, потом по дедлайну

    def __str__(self):
        return f"{self.title} ({'done' if self.is_done else 'pending'})"