from main.api_schemas import *
from ninja import Router
router = Router()
from typing import Optional, List
from services.models import *
from works.models import *



@router.get("/preims/", tags=["Основное"], summary="Список преимуществ", response=List[PreimSchema])
def preims_list(request, service_slug: str = None, homepage: bool = None):
    """ Список преимуществ """

    preims = Preim.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        preims = service.preims.all()

    if homepage:
        homepage = HomePage.objects.all().first()
        preims = homepage.preims.all()

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
def reviews_list(request, service_slug: str = None):
    """ Список отзывов """
    reviews = Review.objects.select_related('source').all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        reviews = service.reviews.all()

    return reviews


@router.get("/faqs/", tags=["Основное"], summary="Список FAQ", response=List[FaqSchema])
def faqs_list(request, service_slug: str = None, homepage: bool = None):
    """ Список FAQS """
    faqs = Faq.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        faqs = service.faqs.all()

    if homepage:
        homepage = HomePage.objects.all().first()
        faqs = homepage.faqs.all()

    return faqs


@router.get("/numbers/", tags=["Основное"], summary="Список цифр", response=List[NumberSchema])
def numbers_list(request, service_slug: str = None, work_slug: str = None, homepage: bool = None, about_company: bool = None):
    """ Список цифр """
    numbers = Number.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        numbers = service.hero_numbers.all()

    if work_slug:
        work = Work.objects.get(slug=work_slug)
        numbers = work.numbers.all()

    if homepage:
        homepage = HomePage.objects.all().first()
        numbers = homepage.hero_numbers.all()

    if about_company:
        homepage = HomePage.objects.all().first()
        numbers = homepage.about_company_numbers.all()
        
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


@router.get("/homepage/", tags=["Основное"], summary="Главная страница", response=HomePageSchema)
def homepage(request):
    """ Главная страница """
    homepage = HomePage.objects.all().first()
    return homepage


@router.get("/history/etaps/", tags=["Основное"], summary="Этапы истории", response=List[HistoryEtapSchema])
def history_etaps_list(request):
    """ Этапы истории """
    history_etaps = HistoryEtap.objects.all()
    return history_etaps



