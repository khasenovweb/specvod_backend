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