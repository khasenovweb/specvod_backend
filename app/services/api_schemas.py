from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from main.models import *
from services.models import *




class ServiceSchema(ModelSchema):
    hero_bg_img_thumb: Optional[str] = None
    textblock_img_thumb: Optional[str] = None
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
        fields = ["name"]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()
    
        

class ServiceMenuSchema(ModelSchema):
    url: Optional[str] = None
    children: Optional[List[ServiceMenuChildSchema]] = []

    class Meta:
        model = Service
        fields = ["name"]

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()



class ServiceChildrenSchema(ModelSchema):
    hero_bg_img_thumb: Optional[str] = None
    url: Optional[str] = None

    class Meta:
        model = Service
        fields = [
            "name",
            "hero_desc",
        ] 

    @staticmethod
    def resolve_hero_bg_img_thumb(obj):
        return (get_thumbnail(obj.hero_bg_img, "407x244", crop="center", quality=99, format="PNG").url if obj.hero_bg_img else None)

    @staticmethod
    def resolve_url(obj):
        return obj.get_url()