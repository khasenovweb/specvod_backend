from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

from main.api_schemas import *
from works.api_schemas import *
from ninja import Router
router = Router()



@router.get("", tags=["Работы"], summary="Список работ", response=List[WorkListingSchema])
def works_list(request, service_slug: str = None, order: str = None):
    """ Список работ """
    works = Work.objects.all()

    if service_slug:
        service = Service.objects.get(slug=service_slug)
        works = works.filter(service__in=service.get_descendants(include_self=True)).distinct()

    if order:
        works = works.order_by(order)
        
    return works


@router.get("{work_slug}/", tags=["Работы"], summary="Работа", response=WorkDetailSchema)
def work(request, work_slug: str):
    """ Работа """
    work = get_object_or_404(Work, slug=work_slug)
    return work


@router.get("{work_slug}/tasks/", tags=["Работы"], summary="Выполненные задачи", response=List[TaskSchema])
def tasks_listing(request, work_slug: str):
    """ Работа """
    work = get_object_or_404(Work, slug=work_slug)
    tasks = Task.objects.filter(work=work)
    return tasks