from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Account


class AccountAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.a1 = Account.objects.create(mobile="2345867845", password="12384", owner="Bob")
        cls.a2 = Account.objects.create(mobile="111111", password="39876", owner="Alice")

    def test_get_accounts(self):
        url = "/api/accounts/"
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsInstance(res.data, list)
        self.assertIn("mobile", res.data[0])
        self.assertIn("password", res.data[0])
        self.assertIn("owner", res.data[0])

    def test_create_account(self):
        url = "/api/accounts/create/"
        payload = {
            "mobile": "874864", 
            "password": "34857945",
            "owner": "Cindy"
        }
        res = self.client.post(url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Account.objects.filter(mobile="874864").exists())

    def test_get_account_detail(self):
        url = f"/api/accounts/{self.a1.pk}/"
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["mobile"], "2345867845")

    def test_update_account(self):
        url = f"/api/accounts/{self.a2.pk}/"
        payload = {   
            "mobile": "2432432",    
            "password": "2222",
            "owner": "David"
        }
        res = self.client.put(url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.a2.refresh_from_db()
        self.assertEqual(self.a2.password, "2222")