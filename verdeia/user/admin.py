from django.contrib import admin
from .models import UserData,Newsletter,VolunteerEvents,UserEvent


# Register your models here.
admin.site.register(UserData)
admin.site.register(Newsletter)
admin.site.register(VolunteerEvents)
admin.site.register(UserEvent)
#admin.site.register(UserGoal)