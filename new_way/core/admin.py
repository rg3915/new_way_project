from django.contrib import admin
from .models import Customer, Employee, Occupation, Dealership, Brand, Modell, Vehicle, \
    Accessory, Kit, KitDetail, Store, Kiosk, Ordered


class CustomerAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Customer model"""
    ordering = ['first_name']
    list_display = ('__str__', 'cpf', 'email', 'phone', 'cell', 'birthday')
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'cpf')
    list_filter = ('gender', 'city')


class EmployeeAdmin(admin.ModelAdmin):
    ordering = ['first_name']
    list_display = ('__str__', 'cpf', 'email', 'phone', 'cell',
                    'occupation', 'created_at', 'comissioned')
    date_hierarchy = 'created_at'
    search_fields = ('first_name', 'last_name', 'cpf')
    list_filter = ('occupation', 'dealership', 'comissioned')


class DealershipAdmin(admin.ModelAdmin):
    ordering = ['dealership']
    list_display = ('dealership', 'phone1', 'phone2', 'district')
    search_fields = ('dealership',)
    # list_filter = ('city',)


class BrandAdmin(admin.ModelAdmin):
    ordering = ['brand']
    list_display = ('brand', 'thumb')


class ModellAdmin(admin.ModelAdmin):
    ordering = ['modell']
    list_display = ('modell', 'brand')
    search_fields = ('modell',)
    list_filter = ('brand',)


class VehicleAdmin(admin.ModelAdmin):
    ordering = ['vehicle']
    readonly_fields = ('image',)
    list_display = (
        'thumb', 'vehicle',  'color', 'year_of_manufacture', 'price', 'kit_fabric')
    search_fields = ('vehicle',)
    list_filter = (
        'modell', 'color', 'year_of_manufacture', 'fueltype', 'transmissiontype')


class AccessoryAdmin(admin.ModelAdmin):
    readonly_fields = ('image',)
    list_display = ('thumb', 'accessory', 'price_accessory')
    search_fields = ('accessory',)


class KitDetailInline(admin.TabularInline):
    list_display = ['kit', 'accessory', 'quantity_accessory']
    model = KitDetail
    extra = 0


class KitAdmin(admin.ModelAdmin):
    inlines = [KitDetailInline]


class StoreAdmin(admin.ModelAdmin):
    ordering = ['store']
    list_display = ('store', 'phone', 'city', 'uf')
    search_fields = ('store',)
    list_filter = ('uf',)


class KioskAdmin(admin.ModelAdmin):
    ordering = ['kiosk']
    list_display = ('kiosk', 'store')
    search_fields = ('kiosk',)


class OrderedAdmin(admin.ModelAdmin):
    ordering = ['-id']
    list_display = ('id', 'customer', 'vehicle', 'dealership',
                    'kiosk', 'employee', 'status', 'created_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    search_fields = ('id', 'customer__first_name', 'customer__last_name', 'vehicle__vehicle',
                     'dealership__dealership', 'kiosk__kiosk')
    list_filter = (
        'status', 'customer__gender', 'dealership__district', 'dealership')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Occupation)
admin.site.register(Dealership, DealershipAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Modell, ModellAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Kit, KitAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Kiosk, KioskAdmin)
admin.site.register(Ordered, OrderedAdmin)
