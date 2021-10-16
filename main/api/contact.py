from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Contact, ContactsSerializer
from rest_framework.views import APIView


class ContactApi(APIView):
    @csrf_exempt
    def put(self, request, id):
        try:
            contact = Contact.objects.get(pk=id)

            name = request.data.get("name", contact.name)
            surname = request.data.get("surname", contact.surname)
            phone = request.data.get("phone", contact.phone)
            address = request.data.get("address", contact.address)
            country = request.data.get("country", contact.country)
            town = request.data.get("town", contact.town)
            street = request.data.get("street", contact.street)
            url = request.data.get("url", contact.url)
            photo = request.data.get("photo", contact.photo)

            contact.name = name
            contact.phone = phone
            contact.surname = surname
            contact.address = address
            contact.country = country
            contact.town = town
            contact.street = street
            contact.url = url
            contact.photo = photo

            contact.save()
        except Contact.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)

        return JsonResponse(ContactsSerializer(contact).data)

    @csrf_exempt
    def delete(self, request, id):
        try:
            contact = Contact.objects.get(pk=id)
            if contact.photo:
                contact.photo.delete()
            contact.delete()
            return JsonResponse(ContactsSerializer(contact).data)
        except Contact.DoesNotExist:
            return HttpResponse('Такого ID не существует', status=404)