from django.contrib import admin
from .models import Donor, Recipient, Donation, Location, Event, Feedback, Branch, Contact

# Register your models here.


admin.site.register(Donor)
admin.site.register(Recipient)
admin.site.register(Donation)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Feedback)
admin.site.register(Branch)
admin.site.register(Contact)  