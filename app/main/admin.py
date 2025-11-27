from django.contrib import admin
from django.utils.html import format_html
from main.models import *

# Register your models here.



@admin.register(Preim)
class PreimAdmin(admin.ModelAdmin):
    pass


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
    pass


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    pass


@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    pass
