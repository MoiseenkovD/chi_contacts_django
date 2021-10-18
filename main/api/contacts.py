from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Contact, ContactsSerializer
from rest_framework.views import APIView
from django.db.models import Q


class ContactsApi(APIView):
    def get(self, request):
        search = request.query_params.get('search')

        if search is not None:
            contacts = Contact.objects.filter(Q(name=search) | Q(surname=search))
        else:
            contacts = Contact.objects.all()

        return JsonResponse(ContactsSerializer(contacts, many=True).data, safe=False)

    @csrf_exempt
    def post(self, request):
        name = request.data.get("name")
        surname = request.data.get("surname")
        phone = request.data.get("phone")
        address = request.data.get("address", "")
        country = request.data.get("country", "")
        town = request.data.get("town", "")
        street = request.data.get("street", "")
        url = request.data.get("url", "")
        photo = request.data.get("photo")

        if name is None or surname is None or phone is None:
            return HttpResponse("Вы не ввели достаточно информации, повторите попытку", status=400)
        else:
            contact = Contact(name=name, surname=surname, phone=phone, address=address,
                         country=country, town=town, street=street, url=url, photo=photo)
        contact.save()
        return JsonResponse(ContactsSerializer(contact).data, status=201)
