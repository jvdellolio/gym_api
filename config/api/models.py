from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=False, blank=False, auto_now=True, editable=False)

class Exercise(models.Model):
    category = models.ForeignKey(on_delete=models.PROTECT, to=Category, related_name="exercises", null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=False, blank=False, auto_now=True, editable=False)