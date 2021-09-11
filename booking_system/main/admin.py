from django.contrib import admin
from main.models import (
    Hall,
    Organization,
    Manager,
    Booking,
    Event
)

# Register your models here.

class HallAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hall._meta.fields]

class ManagerInstance(admin.TabularInline):
    model = Manager
    extra = 1

class OrgAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Organization._meta.fields]
    search_fields = ("name",)
    inlines = [ManagerInstance]

class ManagerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Manager._meta.fields]
    search_fields = ('fullname', "organization__name")

class EventInstance(admin.TabularInline):
    model = Event
    extra = 1

class BookingAdmin(admin.ModelAdmin):
    class Media:
        js = ("admin/js/autocounting.js",)

    def has_change_permission(self, request, obj=None):
        if obj is not None:
            if request.user.role == "admin" or request.user == obj.manager or request.user.is_superuser:
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            if request.user.role == "admin" or request.user == obj.manager or request.user.is_superuser:
                return True
        return False
    search_fields = ("manager__email","status","client__email","start","end","organization__name")
    inlines = [EventInstance]
    list_display = [field.name for field in Booking._meta.fields]

class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]


admin.site.register(Hall, HallAdmin)
admin.site.register(Organization, OrgAdmin)
admin.site.register(Manager, ManagerAdmin)
#admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)