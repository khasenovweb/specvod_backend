from main.api import router as main_router
from services.api import router as services_router
from works.api import router as works_router
from contacts.api import router as contacts_router
from django.conf import settings

from ninja import NinjaAPI

api_v1 = NinjaAPI(
    title="Спецводстрой API",
    version="1.0.0",
    description="Документация",
    docs_url=None if not settings.DEBUG else "/docs",
    openapi_url=None if not settings.DEBUG else "/openapi.json"
)

api_v1.add_router("/main/", main_router)
api_v1.add_router("/services/", services_router)
api_v1.add_router("/works/", works_router)
api_v1.add_router("/contacts/", contacts_router)