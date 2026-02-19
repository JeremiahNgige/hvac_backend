from django.db import models
from categories.models import Category


class Tip(models.Model):
    """Safety tip or maintenance advice for HVAC systems."""
    TIP_TYPE_CHOICES = [
        ('safety', 'Safety'),
        ('maintenance', 'Maintenance'),
        ('energy', 'Energy Saving'),
    ]

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='tips'
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    tip_type = models.CharField(max_length=20, choices=TIP_TYPE_CHOICES, default='maintenance')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
