from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

from main.api_schemas import *
from services.api_schemas import *
from ninja import Router
router = Router()


@router.get("", tags=["Услуги"], summary="Список услуг", response=List[ServiceSchema])
def services_list(request):
    """ Список услуг """
    services = Service.objects.all()
    return services


@router.get("menu/", tags=["Услуги"], summary="Список услуг для меню", response=List[ServiceMenuSchema])
def services_menu(request):
    """ Список услуг для меню """
    services = Service.objects.filter(parent__isnull=True)
    return services


@router.get("{service_slug}/", tags=["Услуги"], summary="Услуга", response=ServiceSchema)
def service(request, service_slug: str):
    """ Услуга """
    subpath = "/".join(request.GET.getlist("subpath"))
    service = get_object_or_404(Service, slug=service_slug)
    service_slugs = service.get_slugs()
    if subpath != service_slugs:
        raise Http404
    return service


@router.get("{service_slug}/breadcrumbs/", tags=["Услуги"], summary="Хлебный крошки услуги", response=List[ServiceBreadcrumbsSchema])
def service_breadcrumbs(request, service_slug: str):
    """ Хлебный крошки услуги """
    service = get_object_or_404(Service, slug=service_slug)
    breadcrumbs = list(service.get_ancestors())
    breadcrumbs.append(service)
    return breadcrumbs


@router.get("{service_slug}/quiz/", tags=["Услуги"], summary="Квиз услуги", response=QuizSchema)
def service_quiz(request, service_slug: str):
    """ Квиз услуги """
    quiz = get_object_or_404(Quiz, service__slug=service_slug)
    return quiz 


@router.get("{service_slug}/childrens/", tags=["Услуги"], summary="Дочерние услуги", response=List[ServiceChildrenSchema])
def service_childrens(request, service_slug: str):
    """ Дочерние услуги """
    service = get_object_or_404(Service, slug=service_slug)
    services = Service.objects.filter(parent=service)
    return services 



