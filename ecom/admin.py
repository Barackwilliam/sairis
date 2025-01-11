from django.contrib import admin
from .models import Customer,Product,Orders,Feedback,Product_1,Product_2,Product_3,Product_4,Product_5
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Product_1, ProductAdmin)
admin.site.register(Product_2, ProductAdmin)
admin.site.register(Product_3, ProductAdmin)
admin.site.register(Product_4, ProductAdmin)
admin.site.register(Product_5, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.




# admin.py

from django.contrib import admin
from .models import HostingStatus

@admin.register(HostingStatus)
class HostingStatusAdmin(admin.ModelAdmin):
    list_display = ('is_active', 'expiration_date', 'is_expired')
    actions = ['activate_hosting', 'deactivate_hosting']

    @admin.action(description='Activate Hosting')
    def activate_hosting(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description='Deactivate Hosting')
    def deactivate_hosting(self, request, queryset):
        queryset.update(is_active=False)