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
        exclude = [
            "policy_text_title",
            "policy_text",
            "cookie_text_title",
            "cookie_text",
        ]

        

class ContactsPolicySchema(ModelSchema):
    class Meta:
        model = Contacts
        fields = [
            "policy_text_title",
            "policy_text",
        ]


class ContactsCookieSchema(ModelSchema):
    class Meta:
        model = Contacts
        fields = [
            "cookie_text_title",
            "cookie_text",
        ]