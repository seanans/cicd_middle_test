from django.test import TestCase, Client
from django.urls import reverse
from .models import Image
from datetime import datetime, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile

class GalleryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a temporary image file for testing
        self.image = Image.objects.create(
            title="Test Image",
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
            created_date=datetime.now().date(),
            age_limit=18
        )

    def test_gallery_view_shows_recent_images(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Image")

    def test_gallery_view_excludes_old_images(self):
        old_image = Image.objects.create(
            title="Old Image",
            image=SimpleUploadedFile("old.jpg", b"file_content", content_type="image/jpeg"),
            created_date=(datetime.now() - timedelta(days=31)).date(),
            age_limit=18
        )
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Old Image")

class ImageDetailViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.image = Image.objects.create(
            title="Detail Image",
            image=SimpleUploadedFile("detail.jpg", b"file_content", content_type="image/jpeg"),
            created_date=datetime.now().date(),
            age_limit=18
        )

    def test_image_detail_view(self):
        response = self.client.get(reverse('image_detail', args=[self.image.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detail Image")