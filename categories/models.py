from django.db import models


class Category(models.Model):
    """HVAC system category (e.g., Furnace, Air Conditioner, Heat Pump)."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Material icon name for Flutter")
    color_hex = models.CharField(max_length=7, default='#0D47A1')

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        return self.name
