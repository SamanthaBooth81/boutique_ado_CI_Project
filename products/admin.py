"""Register models"""
from django.contrib import admin
from .models import Products, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """Product Admin"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
