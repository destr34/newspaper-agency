from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="123admin",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="redactor1234",
            years_of_experience=3
        )

    def test_redactor_years_of_experience_listed(self):
        """Test that redactor's years_of_experience is in
        list_display on redactor admin page"""
        url = reverse("admin:news_agency_redactor_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)

    def test_redactor_detailed_years_of_experience_listed(self):
        """Test that redactor's years_of_experience is on
        redactor_detail admin page"""
        url = reverse(
            "admin:news_agency_redactor_change", args=[self.redactor.id]
        )
        response = self.client.get(url)

        self.assertContains(response, self.redactor.years_of_experience)
