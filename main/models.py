from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(_('Nomi'), max_length=100)
    slug = models.SlugField('*',max_length=150, unique=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = _("KATEGORIYALAR")
        verbose_name_plural = _("KATEGORIYALAR")

    def __str__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField('*',max_length=150, unique=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    sub_title = models.CharField(_("Mavzusi"), max_length=50)
    title = models.CharField(_("Nomi"), max_length=150)
    bg_image = models.ImageField(_("Rasmi"), upload_to=None, height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("SLIDERS")
        verbose_name_plural = _("SLIDERS")

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Kategoriyasi"), related_name='cat_products', on_delete=models.CASCADE)
    name = models.CharField(_('Nomi'),max_length=250)
    slug = models.SlugField('*',max_length=250)
    image = models.ImageField(_('Rasmi'),upload_to='product_images/',blank=False)
    description = models.TextField(_("Ta'rifi"),blank=True)
    price = models.FloatField(_('Narxi'))
    old_price = models.FloatField(_('Avvalgi narxi'), null=True, blank=True)
    instock = models.BooleanField(_('Bor / Yok'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)
        verbose_name = _("MAXSULOTLAR")
        verbose_name_plural = _("MAXSULOTLAR")
    
    def __str__(self):
        return self.name
