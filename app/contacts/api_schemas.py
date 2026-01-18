from typing import List, Optional
from ninja import ModelSchema, Schema, Field
from sorl.thumbnail import get_thumbnail

from contacts.models import *




class OfficeSchema(ModelSchema):
    class Meta:
        model = Office
        fields = "__all__"


class EmployeeSchema(ModelSchema):
    class Meta:
        model = Employee
        fields = "__all__"


class FileSchema(ModelSchema):
    class Meta:
        model = File
        fields = "__all__"


class ContactsSchema(ModelSchema):
    class Meta:
        model = Contacts
        fields = "__all__"