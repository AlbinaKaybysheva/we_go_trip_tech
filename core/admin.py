from django.contrib import admin
from django.utils import timezone
from time import sleep
import requests
import json
from .models import Product, Order, Payment
from .constants import *


@admin.action(description="Confirm selected orders")
def confirm_order(modeladmin, request, queryset):
    for order in queryset:
        if order.payment_set.filter(status=payment_status_paid).exists():
            order.status = order_status_confirmed
            order.confirmed_at = timezone.now()
            order.save()

            sleep(5)
            payload = {
                "id": order.id,
                "amount": str(order.amount),
                "date": order.confirmed_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
            webhook_url = "https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4"
            requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status', 'created_at', 'confirmed_at')
    list_filter = ('status',)
    actions = [confirm_order]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'content', 'price')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'status', 'payment_type', 'order')


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment, PaymentAdmin)
