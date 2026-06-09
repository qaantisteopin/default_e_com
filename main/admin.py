from django.contrib import admin
from .models import Category, Size, Product, \
    ProductImage, ProductSize


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "colour", "price"]
    list_filter = ["category", "colour"]
    search_fields = ["name", "colour", "description"]
    prepopulated_fields = {"slug": ("name", )}
    inlines = [ProductImageInline, ProductSizeInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name", )}


class SizeAdmin(admin.ModelAdmin):
    lis_display = ["name"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)