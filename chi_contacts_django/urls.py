from django.contrib import admin
from django.urls import path
from main.api import contacts
from main.api import contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts.ContactsApi.as_view()),
    path('contacts/<int:id>/', contact.ContactApi.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
