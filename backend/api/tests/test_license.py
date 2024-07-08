from django.test import TestCase
from ninja.testing import TestClient
from api.models.license_models import License
from api.schemas.license_schema import LicenseIn, LicenseOut, LicenseUpdate
from api.routes.license_route import license_router

class LicenseTests(TestCase):
    def setUp(self):
        self.client = TestClient(license_router)
        self.test_license_data = {
            'name': 'Test License'
        }

    def test_create_license(self):
        response = self.client.post("/", json=self.test_license_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], self.test_license_data['name'])

    def test_read_licenses(self):
        license = License.objects.create(name="License 1")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], license.name)

    def test_get_license_by_id(self):
        license = License.objects.create(name="License 1")
        response = self.client.get(f"/{license.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], license.name)

    def test_update_license(self):
        license = License.objects.create(name="License 1")
        update_name = 'Updated License'
        response = self.client.put(f"/{license.id}", json={'name': update_name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], update_name)

    def test_delete_license(self):
        license = License.objects.create(name="License 1")
        response = self.client.delete(f"/{license.id}")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(License.objects.filter(id=license.id).exists())