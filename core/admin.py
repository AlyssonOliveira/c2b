from django.contrib import admin
from core.models import Customer, BuyEvent, Category

class BuyEventAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ( 'description', 'price', 'model_pic', 'image_tag', )
    readonly_fields = ('image_tag',)

admin.site.register(Customer)
admin.site.register(BuyEvent, BuyEventAdmin)
admin.site.register(Category)
