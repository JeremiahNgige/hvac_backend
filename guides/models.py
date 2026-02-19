from django.db import models
from categories.models import Category


class Guide(models.Model):
    """Step-by-step DIY guide for an HVAC task."""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='guides'
    )
    title = models.CharField(max_length=200)
    summary = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    estimated_time = models.CharField(max_length=50, help_text="e.g. '30 minutes', '1-2 hours'")
    image_url = models.URLField(blank=True, default='')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class GuideStep(models.Model):
    """Individual step within a guide."""
    guide = models.ForeignKey(
        Guide, on_delete=models.CASCADE, related_name='steps'
    )
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    pro_tip = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['step_number']
        unique_together = ['guide', 'step_number']

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
