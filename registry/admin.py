from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Authorization, Activity, Manufacturer, Operator, Contact, Aircraft, Pilot, AircraftDetail, AircraftComponent,AircraftComponentSignature
# Register your models here.

admin.site.register(Authorization)
admin.site.register(Activity)
admin.site.register(Manufacturer)
admin.site.register(Operator)
admin.site.register(Contact)
admin.site.register(Pilot)
admin.site.register(Aircraft, SimpleHistoryAdmin)
admin.site.register(AircraftDetail, SimpleHistoryAdmin)
admin.site.register(AircraftComponent, SimpleHistoryAdmin)
admin.site.register(AircraftComponentSignature, SimpleHistoryAdmin)
