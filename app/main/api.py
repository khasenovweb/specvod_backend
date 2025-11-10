from main.api_schemas import *
from ninja import Router
router = Router()



@router.get("/preims/", tags=["Основное"], summary="Список преимуществ", response=List[PreimSchema])
def preims_list(request):
    """ Список преимуществ """
    preims = Preim.objects.all()
    return preims


@router.get("/employees/", tags=["Основное"], summary="Список сотрудников", response=List[EmployeeSchema])
def employee_list(request):
    """ Список сотрудников """
    employess = Employee.objects.all()
    return employess


@router.get("/partners/", tags=["Основное"], summary="Список партнеров", response=List[PartnerSchema])
def partners_list(request):
    """ Список партнеров """
    partners = Partner.objects.all()
    return partners


@router.get("/reviews/", tags=["Основное"], summary="Список отзывов", response=List[ReviewSchema])
def reviews_list(request):
    """ Список отзывов """
    reviews = Review.objects.select_related('source').all()
    return reviews


