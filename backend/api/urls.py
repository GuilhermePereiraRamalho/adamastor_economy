from django.urls import path
from ninja import NinjaAPI
from api.routes.license_route import license_router

api = NinjaAPI()

api.add_router("/license", license_router)

urlpatterns = [
    path("api/", api.urls),
]