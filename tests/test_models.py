from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from news_agency.models import Topic, Redactor, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic_name = Topic.objects.create(topic="test")

        self.assertEqual(str(topic_name), topic_name.topic)

    def test_redactor_str(self):
        redactor = Redactor.objects.create_user(
            username="test",
            password="test12345",
            first_name="Adam",
            last_name="Smith",
            email="adam_smith@.gmail",
        )

        self.assertEqual(
            str(redactor), f"{redactor.first_name} {redactor.last_name}"
        )

    def test_newspaper_str(self) -> None:
        self.user = Redactor.objects.create_user(
            username="test_name",
            password="12345testpassword"
        )
        self.topic = Topic.objects.create(topic="topic_test")
        publishers = [self.user]
        newspaper = Newspaper.objects.create(
            title="www",
            content="test content",
            published_date=timezone.now,
            topic=self.topic,
        )
        newspaper.publishers.set(publishers)
        self.assertEqual(
            str(newspaper),
            f"{newspaper.publishers} published {newspaper.title} date"
            f" {newspaper.published_date}"
        )

    def test_redactor_create_with_years_of_experience(self):
        username = "testVitalii"
        password = "test12345"
        years_of_experience = 3
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )

        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password(password))
        self.assertEqual(redactor.years_of_experience, years_of_experience)