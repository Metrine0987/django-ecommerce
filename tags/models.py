from django.db import models 
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(models.Model):
    label =models.CharField(max_length=255)
    
    def __str__(self):
        return self.label
    
class TaggedItemManager(models.Manager):
    pass
    
class TaggedItem(models.Model):
    tag = models.CharField(max_length=255)

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )