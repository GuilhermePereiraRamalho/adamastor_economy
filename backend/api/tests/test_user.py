from django.test import TestCase
from ninja.testing import TestClient
from api.models.user_models import User
from api.models.license_models import License  
from api.routes.user_route import user_router  

class UserTests(TestCase):
    def setUp(self):
        self.client = TestClient(user_router)
        
        self.license1 = License.objects.create(name='License 1')
        self.license2 = License.objects.create(name='License 2')
        
        self.test_user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'securepassword',
            'license_id': self.license1.id,
        }

    def test_create_user(self):
        response = self.client.post("/", json=self.test_user_data)
        self.assertEqual(response.status_code, 201)  
        self.assertEqual(response.json()['email'], self.test_user_data['email'])

    def test_read_users(self):
        user = User.objects.create_user(**self.test_user_data)
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['email'], self.test_user_data['email'])

    def test_get_user_by_id(self):
        user = User.objects.create_user(**self.test_user_data)
        response = self.client.get(f"/{user.id}") 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['email'], self.test_user_data['email'])

    def test_update_user(self):
        user = User.objects.create_user(**self.test_user_data)
        update_data = {
            'first_name': 'UpdatedName',
            'license_id': self.license2.id,
        }
        response = self.client.put(f"/{user.id}", json=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['first_name'], update_data['first_name'])
        self.assertEqual(response.json()['license_id'], update_data['license_id'])

    def test_delete_user(self):
        user = User.objects.create_user(**self.test_user_data)
        response = self.client.delete(f"/{user.id}")
        self.assertEqual(response.status_code, 204)  
        self.assertFalse(User.objects.filter(id=user.id).exists())  
