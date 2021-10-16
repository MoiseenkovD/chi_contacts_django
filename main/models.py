from django.db import models
from rest_framework import serializers


class Contact(models.Model):
    class Meta:
        db_table = "contacts"

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    photo = models.FileField(upload_to='photos')

    @property
    def image_url(self):
        from django.contrib.sites.models import Site

        domain = Site.objects.get_current().domain
        url = 'http://{domain}'.format(domain=domain)

        if self.photo and hasattr(self.photo, 'url'):
            return url + self.photo.url
        else:
            return ""

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

