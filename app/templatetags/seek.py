from django import template
from django.urls import reverse
from ..models import Picture

register = template.Library()

@register.simple_tag
def seek_instance(lt_or_gt, instance):
    try:
        if lt_or_gt == 'lt':
            inst = Picture.objects.filter(pk__lt=instance.pk).order_by('-pk').first()
            return reverse("app:see_picture", kwargs = {"id":inst.id})
        elif lt_or_gt == 'gt':
            inst = Picture.objects.filter(pk__gt=instance.pk).order_by('pk').first()
            return reverse("app:see_picture", kwargs = {"id":inst.id})
    except Picture.DoesNotExist:
        return reverse("app:see_picture", kwargs = {'id':inst.id})