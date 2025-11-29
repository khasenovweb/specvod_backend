from main.api_schemas import *
from ninja import Router
router = Router()
from typing import Optional, List
from services.models import *



@router.get("/preims/", tags=["Основное"], summary="Список преимуществ", response=List[PreimSchema])
def preims_list(request, service_slug: str = None):
    """ Список преимуществ """

    preims = Preim.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        preims = service.preims.all()

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


@router.get("/faqs/", tags=["Основное"], summary="Список FAQ", response=List[FaqSchema])
def faqs_list(request):
    """ Список FAQS """
    faqs = Faq.objects.all()
    return faqs


@router.get("/numbers/", tags=["Основное"], summary="Список цифр", response=List[NumberSchema])
def numbers_list(request, service_slug: str = None):
    """ Список цифр """
    numbers = Number.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        numbers = service.hero_numbers.all()
        
    return numbers


@router.get("/sertificates/", tags=["Основное"], summary="Список сертификатов", response=List[SertificateSchema])
def sertificates_list(request, service_slug: str = None):
    """ Список сертификатов """
    sertificates = Sertificate.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        sertificates = service.sertificates.all()
        
    return sertificates


@router.get("/promotions/", tags=["Основное"], summary="Список акций", response=List[PromotionSchema])
def promotions_list(request, service_slug: str = None):
    """ Список акций """
    promotions = Promotion.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        promotions = service.promotions.all()
        
    return promotions


@router.get("/price/", tags=["Основное"], summary="Список позиций прайса", response=List[PricePositionSchema])
def price_positions_list(request, service_slug: str = None):
    """ Список позици прайса """
    positions = PricePosition.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        positions = service.price_positions.all()
        
    return positions


@router.get("/methods/", tags=["Основное"], summary="Список методов бурения", response=List[MethodSchema])
def methods_list(request, service_slug: str = None):
    """ Список методов бурения """
    methods = Method.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        methods = service.methods.all()
        
    return methods


@router.get("/technics/", tags=["Основное"], summary="Список техники", response=List[TechnicSchema])
def technics_list(request, service_slug: str = None):
    """ Список техники """
    technics = Technic.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        technics = service.technics.all()
        
    return technics


@router.get("/etaps/", tags=["Основное"], summary="Список этапов", response=List[EtapSchema])
def etaps_list(request, service_slug: str = None):
    """ Список этапов """
    etaps = Etap.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        etaps = service.etaps.all()
        
    return etaps



