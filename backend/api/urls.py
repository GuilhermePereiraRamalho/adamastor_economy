from django.urls import path
from ninja import NinjaAPI
from api.routes.license_route import license_router
from api.routes.user_route import user_router

api = NinjaAPI()

api.add_router("/licenses", license_router)
api.add_router("/users", user_router)

urlpatterns = [
    path("api/", api.urls),
]