from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __unicode__(self):
        return "<%s>" %self.name

class Location(models.Model):
    place = models.CharField(max_length=100, db_index=True, unique=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "<%s>" %self.place

class Item(models.Model):
    name = models.CharField(max_length=300)
    slug_name = models.SlugField(max_length=300)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    special_info = models.TextField(blank=True, null=True)

    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return "<%s-%s-%s>" %(self.name, self.category.name, \
                              self.location.place)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(Item, self).save(*args, **kwargs)
