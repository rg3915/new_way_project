from django.contrib import admin
from .models import Customer, Employee, Occupation, Address, Dealership, Brand, Modell, Vehicle, \
    Accessory, Kit, Store, Kiosk, Ordered


class CustomerAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Customer model"""
    ordering = ['first_name']
    list_display = ('__str__', 'cpf', 'email', 'phone', 'cell', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'cpf')


class EmployeeAdmin(admin.ModelAdmin):

    ordering = ['first_name']
    list_display = ('__str__', 'cpf', 'email', 'phone', 'cell',
                    'occupation', 'created_at', 'comissioned')
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'cpf')
    list_filter = ('occupation', 'dealership', 'comissioned')


class DealershipAdmin(admin.ModelAdmin):

    ordering = ['dealership']
    list_display = ('dealership', 'phone1', 'phone2', 'phone3')
    search_fields = ('dealership',)
    # list_filter = ('city',)


class ModellAdmin(admin.ModelAdmin):

    ordering = ['modell']
    list_display = ('modell', 'brand')
    search_fields = ('modell',)
    list_filter = ('brand',)


class VehicleAdmin(admin.ModelAdmin):

    ordering = ['vehicle']
    list_display = (
        'vehicle', 'color', 'year_of_manufacture', 'price', 'kit_fabric')
    search_fields = ('vehicle',)
    list_filter = (
        'modell', 'color', 'year_of_manufacture', 'fueltype', 'transmissiontype')


class StoreAdmin(admin.ModelAdmin):

    ordering = ['store']
    list_display = ('store', 'phone', 'city', 'uf')
    search_fields = ('store',)
    list_filter = ('city', 'uf')


class KioskAdmin(admin.ModelAdmin):

    ordering = ['kiosk']
    list_display = ('kiosk', 'store')
    search_fields = ('kiosk', 'store')
    list_filter = ('store',)


class OrderedAdmin(admin.ModelAdmin):

    ordering = ['-created_at']
    list_display = (
        'customer', 'vehicle', 'dealership', 'kiosk', 'employee', 'status')
    date_hierarchy = 'created_at'
    search_fields = ('customer', 'vehicle', 'dealership', 'kiosk')
    list_filter = ('dealership', 'kiosk', 'status')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Occupation)
admin.site.register(Address)
admin.site.register(Dealership, DealershipAdmin)
admin.site.register(Brand)
admin.site.register(Modell, ModellAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Accessory)
admin.site.register(Kit)
admin.site.register(Store, StoreAdmin)
admin.site.register(Kiosk, KioskAdmin)
admin.site.register(Ordered, OrderedAdmin)
