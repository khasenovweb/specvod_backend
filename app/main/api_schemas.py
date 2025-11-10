from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from main.models import *


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