<<<<<<< HEAD
import py_compile
from pathlib import Path
from unittest.mock import patch

from django.core import mail
from django.test import SimpleTestCase, override_settings
=======
from django.core import mail
from django.test import override_settings
>>>>>>> esgtest-r/main
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User

<<<<<<< HEAD
=======
from v1.parsers.NlpMethods import ESG_SUBGENRES

>>>>>>> esgtest-r/main
from .models import Comment, News, Subscriber


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class SubscriptionAndAdminTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="regular",
            email="regular@example.com",
            password="StrongPass123",
            is_active=True,
            is_email_verified=True,
        )
        self.admin = User.objects.create_user(
            username="admin",
            email="admin@example.com",
            password="StrongPass123",
            is_active=True,
            is_email_verified=True,
            is_staff=True,
        )

    def authenticate(self, user):
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")

    def test_subscription_confirmation_and_news_notification(self):
        self.authenticate(self.user)

        subscribe_response = self.client.post("/api/v1/subscribe/")
        self.assertEqual(subscribe_response.status_code, status.HTTP_201_CREATED)

        subscriber = Subscriber.objects.get(email=self.user.email)
        self.assertFalse(subscriber.is_active)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(str(subscriber.confirm_token), mail.outbox[0].body)

        confirm_response = self.client.get(f"/api/v1/subscribe/confirm/{subscriber.confirm_token}/")
        self.assertEqual(confirm_response.status_code, status.HTTP_200_OK)

        subscriber.refresh_from_db()
        self.assertTrue(subscriber.is_active)
<<<<<<< HEAD
=======
        self.assertEqual(subscriber.genre_preferences, list(ESG_SUBGENRES))
>>>>>>> esgtest-r/main

        self.client.credentials()
        self.authenticate(self.admin)
        news_payload = {
            "title": "Major ESG Update",
            "digest": "Digest text",
            "site_url": "https://example.com/news",
            "lang": "en",
        }
        news_response = self.client.post("/api/v1/admin/news/", news_payload, format="json")
        self.assertEqual(news_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(len(mail.outbox), 2)
        self.assertIn("Major ESG Update", mail.outbox[1].subject)
        self.assertIn(self.user.email, mail.outbox[1].to)

<<<<<<< HEAD
=======
    def test_subscription_preferences_update(self):
        self.authenticate(self.user)
        self.client.post("/api/v1/subscribe/")
        subscriber = Subscriber.objects.get(email=self.user.email)
        self.client.get(f"/api/v1/subscribe/confirm/{subscriber.confirm_token}/")

        preferences_response = self.client.get("/api/v1/subscribe/preferences/")
        self.assertEqual(preferences_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(preferences_response.data["available_genres"]), 5)
        self.assertTrue(preferences_response.data["is_active"])

        update_response = self.client.patch(
            "/api/v1/subscribe/preferences/",
            {"genre_preferences": ["climate", "waste"]},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["genre_preferences"], ["climate", "waste"])

        subscriber.refresh_from_db()
        self.assertEqual(subscriber.genre_preferences, ["climate", "waste"])

    def test_genre_filtered_news_notification(self):
        self.authenticate(self.user)
        self.client.post("/api/v1/subscribe/")
        subscriber = Subscriber.objects.get(email=self.user.email)
        self.client.get(f"/api/v1/subscribe/confirm/{subscriber.confirm_token}/")
        subscriber.genre_preferences = ["labor"]
        subscriber.save(update_fields=["genre_preferences"])

        self.client.credentials()
        self.authenticate(self.admin)

        climate_news = {
            "title": "Солнечная электростанция",
            "digest": "Снижение выбросов углерода",
            "site_url": "https://example.com/climate",
            "lang": "ru",
        }
        climate_response = self.client.post("/api/v1/admin/news/", climate_news, format="json")
        self.assertEqual(climate_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 1)

        labor_news = {
            "title": "Забастовка на заводе",
            "digest": "Рабочие требуют повышения зарплаты",
            "site_url": "https://example.com/labor",
            "lang": "ru",
        }
        labor_response = self.client.post("/api/v1/admin/news/", labor_news, format="json")
        self.assertEqual(labor_response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 2)
        self.assertIn(self.user.email, mail.outbox[1].to)
        self.assertIn("Забастовка", mail.outbox[1].subject)

>>>>>>> esgtest-r/main
    def test_admin_dashboard_and_comment_moderation(self):
        news = News.objects.create(
            title="Public news",
            digest="Digest text",
            site_url="https://example.com/public-news",
            lang="en",
        )
        comment = Comment.objects.create(user=self.user, news=news, text="Please review", is_approved=False)

        self.authenticate(self.user)
        forbidden_response = self.client.get("/api/v1/admin/dashboard/")
        self.assertEqual(forbidden_response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials()
        self.authenticate(self.admin)

        dashboard_response = self.client.get("/api/v1/admin/dashboard/")
        self.assertEqual(dashboard_response.status_code, status.HTTP_200_OK)
        self.assertEqual(dashboard_response.data["users"], 2)
        self.assertEqual(dashboard_response.data["news_count"], 1)

        comment_response = self.client.patch(
            f"/api/v1/admin/comments/{comment.id}/",
            {"is_approved": True},
            format="json",
        )
        self.assertEqual(comment_response.status_code, status.HTTP_200_OK)

        comment.refresh_from_db()
        self.assertTrue(comment.is_approved)
<<<<<<< HEAD


class SecurityRegressionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="security-user",
            email="security-user@example.com",
            password="StrongPass123",
            is_active=True,
            is_email_verified=True,
        )
        self.admin = User.objects.create_user(
            username="security-admin",
            email="security-admin@example.com",
            password="StrongPass123",
            is_active=True,
            is_email_verified=True,
            is_staff=True,
        )

    def authenticate(self, user):
        token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")

    @override_settings(DEBUG=False)
    def test_parser_run_requires_admin_when_debug_is_disabled(self):
        remote_addr = "203.0.113.10"

        with patch("v1.views.run_all_parsers") as mocked_run:
            anonymous_response = self.client.post(
                "/api/v1/parsers/run/",
                {"mode": "sync"},
                format="json",
                REMOTE_ADDR=remote_addr,
            )
            self.assertEqual(anonymous_response.status_code, status.HTTP_401_UNAUTHORIZED)

            self.authenticate(self.user)
            user_response = self.client.post(
                "/api/v1/parsers/run/",
                {"mode": "sync"},
                format="json",
                REMOTE_ADDR=remote_addr,
            )
            self.assertEqual(user_response.status_code, status.HTTP_403_FORBIDDEN)

            self.client.credentials()
            self.authenticate(self.admin)
            admin_response = self.client.post(
                "/api/v1/parsers/run/",
                {"mode": "sync"},
                format="json",
                REMOTE_ADDR=remote_addr,
            )
            self.assertEqual(admin_response.status_code, status.HTTP_200_OK)

        mocked_run.assert_called_once()

    def test_content_write_requires_admin_role(self):
        payload = {
            "title": "Blocked write",
            "digest": "Regular users should not create news",
            "site_url": "https://example.com/security",
            "lang": "en",
        }

        self.authenticate(self.user)
        user_response = self.client.post("/api/v1/News/", payload, format="json")
        self.assertEqual(user_response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials()
        self.authenticate(self.admin)
        admin_response = self.client.post("/api/v1/News/", payload, format="json")
        self.assertEqual(admin_response.status_code, status.HTTP_201_CREATED)


class SyntaxRegressionTests(SimpleTestCase):
    def test_live_project_python_files_compile(self):
        project_root = Path(__file__).resolve().parents[1]
        source_roots = [
            project_root / "ESGBack",
            project_root / "user",
            project_root / "v1",
        ]

        python_files = [
            path
            for source_root in source_roots
            for path in source_root.rglob("*.py")
            if "__pycache__" not in path.parts
        ]

        self.assertGreater(len(python_files), 0)

        for path in python_files:
            with self.subTest(path=path.relative_to(project_root)):
                py_compile.compile(str(path), doraise=True)
=======
>>>>>>> esgtest-r/main
