from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

from main.api_schemas import *
from services.api_schemas import *
from contacts.api_schemas import *

from ninja import Router
router = Router()




@router.get("/offices/", tags=["Контакты"], summary="Список офисов", response=List[OfficeSchema])
def offices_list(request):
    """ Список офисов """
    offices = Office.objects.all()
    return offices


@router.get("/employees/", tags=["Контакты"], summary="Список сотрудников", response=List[EmployeeSchema])
def employees_list(request):
    """ Список сотрудников """
    employees = Employee.objects.all()
    return employees


@router.get("/files/", tags=["Контакты"], summary="Список файлов", response=List[FileSchema])
def files_list(request):
    """ Список файлов """
    files = File.objects.all()
    return files


@router.get("", tags=["Контакты"], summary="Основные контакты", response=ContactsSchema)
def contacts(request):
    """ Основные контакты """
    contacts = Contacts.objects.all().first()
    if contacts:
        return contacts
    else:
        default_contacts = Contacts()
        default_contacts.adress = "-"
        default_contacts.phone_1 = "-"
        default_contacts.adress_link = "-"
        default_contacts.phone_2 = "-"
        default_contacts.vk = "-"
        default_contacts.whatsapp = "-"
        default_contacts.conpany_name = "-"
        default_contacts.inn_kpp = "-"
        default_contacts.ogrn = "-"
        return default_contacts