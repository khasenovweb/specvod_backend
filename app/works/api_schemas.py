from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from main.models import *
from services.models import *
from works.models import *

import locale

try:
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
except:
    locale.setlocale(locale.LC_ALL, 'ru_RU')


class WorkListingSchema(ModelSchema):
    url: Optional[str] = None
    img_thumb: Optional[str] = None
    date: Optional[str] = ""

    class Meta:
        model = Work
        fields = [
            "name",
            "text",
            "client",
            "map_marker",
        ]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "710x300", crop="center", quality=99, format="PNG").url if obj.img else None)
    
    @staticmethod
    def resolve_date(obj):
        return obj.date.strftime("%d %B %Y") if obj.date else ""

        
class WorkDetailSchema(ModelSchema):
    url: Optional[str] = None
    img_thumb: Optional[str] = None

    class Meta:
        model = Work
        fields = [
            "name",
            "text",
        ]

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "1500", quality=99, format="PNG").url if obj.img else None)

        
class TaskSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Task
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "470x470", crop="center", quality=99, format="PNG").url if obj.img else None)