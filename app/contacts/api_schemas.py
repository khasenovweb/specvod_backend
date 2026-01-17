from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from contacts.models import *




class OfficeSchema(ModelSchema):
    class Meta:
        model = Office
        fields = "__all__"