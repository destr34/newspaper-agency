from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from news_agency.models import Topic, Newspaper, Redactor


TOPIC_URL = reverse("news_agency:topic-list")
REDACTOR_URL = reverse("news_agency:redactor-list")
NEWSPAPER_URL = reverse("news_agency:newspaper-list")

class PublicTopicTests(TestCase):
    def test_login_required(self) -> None:
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123",
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self) -> None:
        Topic.objects.create(topic="news_test")
        Topic.objects.create(topic="news_test2")

        response = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "news_agency/topic_list.html")


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test_name",
            "test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_newspaper(self) -> None:
        topic = Topic.objects.create(topic="Test_topic")
        Newspaper.objects.create(
            topic=topic,
            title="test_title",
            content="Loren ipsum",
        )

        newspaper = Newspaper.objects.all()
        response = self.client.get(NEWSPAPER_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspaper)
        )


class PublicRedactorTests(TestCase):
        def test_login_required(self) -> None:
            res = self.client.get(REDACTOR_URL)

            self.assertNotEqual(res.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "Adam_test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_redactor(self) -> None:
        Redactor.objects.create_user(
            "Sam",
            "test1234",
        )
        redactor = Redactor.objects.all()
        response = self.client.get(REDACTOR_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(redactor)
        )

    def test_create_redactor(self):
        form_data = {
            "username": "new_user",
            "password1": "test1233",
            "password2": "test1233",
            "first_name": "Jakob",
            "last_name": "Smith",
            "years_of_experience": 5
        }
        self.client.post(reverse("news_agency:redactor-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])\
