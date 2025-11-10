from main.api import router as main_router

from ninja import NinjaAPI

api_v1 = NinjaAPI(
    title="Спецводстрой API",
    version="1.0.0",
    description="Документация",
)

api_v1.add_router("/main/", main_router)