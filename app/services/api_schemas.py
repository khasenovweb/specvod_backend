from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from main.models import *
from services.models import *




class ServiceSchema(ModelSchema):
    hero_bg_img_thumb: Optional[str] = None
    textblock_img_thumb: Optional[str] = None
    methods_bg_thumb: Optional[str] = None
    etaps_img_thumb: Optional[str] = None
    url: Optional[str] = None

    class Meta:
        model = Service
        fields = "__all__"

    @staticmethod
    def resolve_hero_bg_img_thumb(obj):
        return (get_thumbnail(obj.hero_bg_img, "1920", quality=99, format="PNG").url if obj.hero_bg_img else None)

    @staticmethod
    def resolve_textblock_img_thumb(obj):
        return (get_thumbnail(obj.textblock_img, "520x520", crop="center", quality=99, format="PNG").url if obj.textblock_img else None)

    @staticmethod
    def resolve_methods_bg_thumb(obj):
        return (get_thumbnail(obj.methods_bg, "1920", quality=99, format="PNG").url if obj.methods_bg else None)

    @staticmethod
    def resolve_etaps_img_thumb(obj):
        return (get_thumbnail(obj.etaps_img, "520x520", crop="center", quality=99, format="PNG").url if obj.etaps_img else None)

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()



class ServiceBreadcrumbsSchema(ModelSchema):
    url: Optional[str] = None

    class Meta:
        model = Service
        fields = ["name"]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()


class ServiceMenuChildSchema(ModelSchema):
    url: Optional[str] = None

    class Meta:
        model = Service
        fields = ["name", "price"]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()
    
        

class ServiceMenuSchema(ModelSchema):
    url: Optional[str] = None
    children: Optional[List[ServiceMenuChildSchema]] = []

    class Meta:
        model = Service
        fields = ["slug", "name", "price"]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()


class PropertySchema(ModelSchema):
    class Meta:
        model = Property
        fields = "__all__"


class ServiceChildrenSchema(ModelSchema):
    hero_bg_img_thumb: Optional[str] = None
    url: Optional[str] = None
    properties: List[PropertySchema] = []

    class Meta:
        model = Service
        fields = [
            "name",
            "hero_desc",
            "name_listing",
            "desc_listing",
            "price",
        ] 

    @staticmethod
    def resolve_hero_bg_img_thumb(obj):
        return (get_thumbnail(obj.hero_bg_img, "407x244", crop="center", quality=99, format="PNG").url if obj.hero_bg_img else None)

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()