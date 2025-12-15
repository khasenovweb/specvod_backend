from django.contrib import admin
from django.utils.html import format_html
from main.models import *

# Register your models here.



@admin.register(Preim)
class PreimAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'order',
    ]
    list_editable = [
        'order', 
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    fields = [
        'img',
        'display_img_preview',
        'fio',
        'role',
        'order',
    ]
    list_display = [
        'display_img_preview',
        'fio',
        'role',
        'order',
    ]
    list_editable = [
        'order', 
    ]
    readonly_fields = [
        'display_img_preview'
    ]
    search_fields = [
        'fio'
    ]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    fields = [
        'img',
        'display_img_preview',
        'title',
        'order',
    ]
    list_display = [
        'display_img_preview',
        'title',
        'order',
    ]
    list_editable = [
        'order', 
    ]
    readonly_fields = [
        'display_img_preview'
    ]
    search_fields = [
        'title'
    ]

    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'user_name',
        'source',
        'rating',
        'date',
    ]
    list_filter = [
        'source',
        'rating',
        'date', 
    ]
    search_fields = [
        'user_name',
    ]


@admin.register(ReviewSource)
class ReviewSourceAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    readonly_fields = [
        'display_img_preview'
    ]
    fields = [
        "name",
        "img",
        "display_img_preview",
    ]
    list_display = [
        "display_img_preview", 
        "name",
    ]



@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'order',
    ]
    list_editable = [
        'order', 
    ]


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'order', 
    ]
    list_editable = [
        'order', 
    ]


@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"

    list_display = [
        'display_img_preview',
        'name',
        'order',
    ]
    readonly_fields = [
        'display_img_preview', 
    ]
    list_editable = [
        'order', 
    ]
    


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"

    list_display = [
        'display_img_preview',
        'name',
    ]
    readonly_fields = [
        'display_img_preview', 
    ]


@admin.register(PricePosition)
class PricePositionAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"

    readonly_fields = [
        'display_img_preview',
    ]

    list_display = [
        'name', 
        'display_img_preview', 
        'price', 
        'order', 
    ]
    list_editable = [
        'order',  
    ]


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    readonly_fields = [
        'display_img_preview',
    ]
    list_display = [
        'display_img_preview',
        'title',
        'order',
    ]
    list_editable = [
        'order',    
    ]


@admin.register(Technic)
class TechnicAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    readonly_fields = [
        'display_img_preview',
    ]
    list_display = [
        'display_img_preview',
        'title',
        'order',
    ]
    list_editable = [
        'order',    
    ]


@admin.register(Etap)
class EtapAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'order',
    ]
    list_editable = [
        'order', 
    ]


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    filter_horizontal = [
        "hero_numbers",
        "preims",
        "about_company_numbers",
        "history_etaps",
        "faqs",
    ]


@admin.register(HistoryEtap)
class HistoryEtapAdmin(admin.ModelAdmin):
    @admin.display(description='Превью')
    def display_img_preview(self, obj):
        if obj.img:
            return format_html(
                f'<img src="{obj.img.url}" style="max-height: 50px; max-width: 50px;" />',
            )
        return "Нет изображения"
    readonly_fields = [
        'display_img_preview',
    ]
    list_display = [
        'display_img_preview',
        'title',
        'order',
    ]
    list_editable = [
        'order', 
    ]
