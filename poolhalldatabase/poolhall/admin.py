from django.contrib import admin
from .models import User, Event, Table, AllTables

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Table)
admin.site.register(AllTables)
