# admin.py
from django.contrib import admin
from .models.product import Product, Size, Color, Photos, Review, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'title_az', 'price', 'short_description_ru', 'short_description_az',
                    'full_description_ru', 'full_description_az', 'trading', 'sale', 'category']

    list_filter = ['trading', 'sale', 'category']
    search_fields = ['title_ru', 'title_az']
    filter_horizontal = ['size', 'color', 'photos', 'reviews']

    fieldsets = [
        ('Main Information', {'fields': ['title_ru', 'title_az', 'price']}),
        ('Descriptions',
         {'fields': ['short_description_ru', 'short_description_az', 'full_description_ru', 'full_description_az']}),
        ('Options', {'fields': ['color', 'size']}),
        ('Media', {'fields': ['main_photo', 'photos']}),
        ('Settings', {'fields': ['trading', 'sale', 'reviews']}),
        ('Category', {'fields': ['category']}),
    ]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'size' or db_field.name == 'color' or db_field.name == 'photos' or db_field.name == 'reviews':
            kwargs['queryset'] = db_field.related_model.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            # Set defaults for new products
            obj.trading = False

        # Update the price based on the discount
        obj.price = obj.price - (obj.price * obj.sale / 100.0)

        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Photos)
admin.site.register(Review)
admin.site.register(Category)
