from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    image = models.CharField(default='0')
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField(default='False')
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

