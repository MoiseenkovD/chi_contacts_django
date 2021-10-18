from django.db import models
from rest_framework import serializers


class Contact(models.Model):
    class Meta:
        db_table = "contacts"
        unique_together = ('name', 'surname')

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    photo = models.FileField(upload_to='photos')

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

