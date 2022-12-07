from django.db import models
# from .validators import validate_of_units
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Recipe(TimeStamp):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True, null=True)
    # tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RecipeIngredient(TimeStamp):
    UNITS = (
        (0, 'kg'),  # get_<fielld_name>_display
        (1, 'l'),
        (2, 'sht')
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=210, help_text='kamroq soz bilan tarifla', null=True)
    quantity = models.FloatField()
    # unit=models.CharField(max_length=22,validators=[validate_of_units])  #kg,l,sht
    unit = models.IntegerField(choices=UNITS, default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


def recipe_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(f"{instance.user_id} {instance.name}")
        instance.save()


post_save.connect(recipe_post_save, sender=Recipe)
