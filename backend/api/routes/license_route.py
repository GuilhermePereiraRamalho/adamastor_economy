from ninja import Router
from api.models.license_models import License
from api.schemas.license_schema import LicenseIn, LicenseUpdate, LicenseOut
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404

license_router = Router(tags=["Licenses"])

@license_router.post("/", response={201: LicenseOut})
def create_license(request, license_in: LicenseIn):
    license = License.objects.create(**license_in.dict())
    return 201, LicenseOut.from_orm(license)

@license_router.get("/", response=list[LicenseOut])
def read_licenses(request):
    licenses = License.objects.all().order_by('id')
    return [LicenseOut.from_orm(license) for license in licenses]

@license_router.get("/{license_id}", response={200: LicenseOut})
def get_license_by_id(request, license_id: int):
    license = get_object_or_404(License, id=license_id)
    return LicenseOut.from_orm(license)

@license_router.put("/{license_id}", response={200: LicenseOut})
def update_license(request, license_id: int, license_in: LicenseUpdate):
    license = get_object_or_404(License, id=license_id)

    for attr, value in license_in.dict().items():
        setattr(license, attr, value)
    license.save()
    return LicenseOut.from_orm(license)

@license_router.delete("/{license_id}", response={204: None})
def delete_license(request, license_id: int):
    license = get_object_or_404(License, id=license_id)
    license.delete()
    return 204, None