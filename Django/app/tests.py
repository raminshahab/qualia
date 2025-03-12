from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import TeamMember


class TeamMemberAPITests(APITestCase):
    def setUp(self):
        self.team_member1 = TeamMember.objects.create(
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="john.doe@example.com",
            role="regular",
        )
        self.team_member2 = TeamMember.objects.create(
            first_name="Jane",
            last_name="Smith",
            phone="0987654321",
            email="jane.smith@example.com",
            role="admin",
        )

    def test_list_team_members(self):
        url = reverse("teammember-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 5)

    def test_create_team_member(self):
        url = reverse("teammember-list")
        data = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "phone": "5555555555",
            "email": "alice.johnson@example.com",
            "role": "regular",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TeamMember.objects.count(), 7)

    def test_create_team_member_invalid_phone(self):
        url = reverse("teammember-list")
        data = {
            "first_name": "Bob",
            "last_name": "Brown",
            "phone": "12345",
            "email": "bob.brown@example.com",
            "role": "regular",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("phone", response.data)

    def test_retrieve_team_member(self):
        url = reverse("teammember-detail", args=[self.team_member1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "John")

    def test_update_team_member(self):
        url = reverse("teammember-detail", args=[self.team_member1.id])
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone": "1234567890",
            "email": "john.doe@example.com",
            "role": "admin",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["role"], "admin")

    def test_delete_team_member(self):
        url = reverse("teammember-detail", args=[self.team_member1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TeamMember.objects.count(), 5)

    def test_search_team_members(self):
        url = reverse("teammember-list")
        response = self.client.get(url, {"search": "john"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)
        self.assertEqual(response.data["results"][0]["first_name"], "John")

    def test_filter_team_members_by_role(self):
        url = reverse("teammember-list")
        response = self.client.get(url, {"role": "admin"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 3)
        self.assertEqual(response.data["results"][0]["first_name"], "John")