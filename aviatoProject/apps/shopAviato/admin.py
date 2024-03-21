# admin.py
from django.contrib import admin
from .models.product import Product, Size, Color, Photos, Review, Category, ContactForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_ru', 'title_az', 'title_en', 'price', 'quantity', 'short_description_ru', 'short_description_az',
                    'full_description_ru', 'full_description_az', 'trending', 'sale', 'category']

    list_filter = ['trending', 'sale', 'category']
    search_fields = ['title_ru', 'title_az', 'title_en']
    filter_horizontal = ['size', 'color', 'photos', 'reviews']

    fieldsets = [
        ('Main Information', {'fields': ['title_ru', 'title_az', 'title_en', 'price', 'quantity']}),
        ('Descriptions',
         {'fields': ['short_description_ru', 'short_description_az', 'full_description_ru', 'full_description_az']}),
        ('Options', {'fields': ['color', 'size']}),
        ('Media', {'fields': ['main_photo', 'photos']}),
        ('Settings', {'fields': ['trending', 'sale', 'reviews']}),
        ('Category', {'fields': ['category']}),
    ]

    class ContactFormAdmin(admin.ModelAdmin):
        list_display = ['fullname', 'contacts', 'message']
        search_fields = ['fullname', 'contacts', 'message']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'size' or db_field.name == 'color' or db_field.name == 'photos' or db_field.name == 'reviews':
            kwargs['queryset'] = db_field.related_model.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.price = obj.price - (obj.price * obj.sale / 100.0)
        super().save_model(request, obj, form, change)


admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Photos)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(ContactForm)