from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=40)
    original_link = models.BooleanField(default=False, verbose_name='Link to original image',
                                        help_text='Can user see the link to an original image?')
    expiring_links = models.BooleanField(default=False, verbose_name='Expiring links',
                                         help_text='Can user create expiring links?')
    size = models.ManyToManyField('Size', related_name='tier')

    def __str__(self):
        return f'{self.name}'


class Size(models.Model):
    height = models.PositiveIntegerField(default=200, verbose_name='Height in px')

    def __str__(self):
        return f'{self.height} px'
