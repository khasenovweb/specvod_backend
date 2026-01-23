from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from main.models import *
from services.api_schemas import ServiceMenuSchema, ServiceMenuChildSchema


class PreimSchema(ModelSchema):
    class Meta:
        model = Preim
        fields = "__all__"


class EmployeeSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Employee
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "344x344", crop="center", quality=99, format="PNG").url if obj.img else None)

        
class PartnerSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Partner
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "344x344", crop="center", quality=99, format="PNG").url if obj.img else None)


class ReviewSourceSchema(ModelSchema):

    class Meta:
        model = ReviewSource
        fields = "__all__"


class ReviewSchema(ModelSchema):
    source: ReviewSourceSchema

    class Meta:
        model = Review
        fields = "__all__"
        exclude = ['source']

        
class FaqSchema(ModelSchema):

    class Meta:
        model = Faq
        fields = "__all__"
        # exclude = ['source']


class NumberSchema(ModelSchema):

    class Meta:
        model = Number
        fields = "__all__"


class SertificateSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Sertificate
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "344", quality=99, format="PNG").url if obj.img else None)

        
class QuizSchema(ModelSchema):

    class Meta:
        model = Quiz
        fields = "__all__"
        

class PromotionSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Promotion
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "700", quality=99, format="PNG").url if obj.img else None)


        
class PricePositionSchema(ModelSchema):

    class Meta:
        model = PricePosition
        fields = "__all__"

        
class MethodSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Method
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "520x520", crop="center", quality=99, format="PNG").url if obj.img else None)

        
class TechnicSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = Technic
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "700", quality=99, format="PNG").url if obj.img else None)
        

class EtapSchema(ModelSchema):

    class Meta:
        model = Etap
        fields = "__all__"



class HomePageSchema(ModelSchema):
    hero_bg_img_thumb: Optional[str] = None
    about_company_img_thumb: Optional[str] = None

    class Meta:
        model = HomePage
        fields = "__all__"

    @staticmethod
    def resolve_hero_bg_img_thumb(obj):
        return (get_thumbnail(obj.hero_bg_img, "1920", quality=99, format="PNG").url if obj.hero_bg_img else None)

    @staticmethod
    def resolve_about_company_img_thumb(obj):
        return (get_thumbnail(obj.about_company_img, "520x520", crop="center", quality=99, format="PNG").url if obj.about_company_img else None)



class HistoryEtapSchema(ModelSchema):
    img_thumb: Optional[str] = None

    class Meta:
        model = HistoryEtap
        fields = "__all__"

    @staticmethod
    def resolve_img_thumb(obj):
        return (get_thumbnail(obj.img, "500x500", crop="center", quality=99, format="PNG").url if obj.img else None)

        
class SearchSchema(Schema):
    services: List[ServiceMenuChildSchema] = []



class AnchorSchema(ModelSchema):

    class Meta:
        model = Anchor
        fields = "__all__"