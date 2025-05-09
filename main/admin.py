from django.contrib import admin
from .models import usser
from .models import Sitetext
from .models import ContactRequest
from .models import ContactRequest2

admin.site.register(usser)

admin.site.register(Sitetext)
class SiteTextAdmin(admin.ModelAdmin):
    list_display=('title')

admin.site.register(ContactRequest)

admin.site.register(ContactRequest2)