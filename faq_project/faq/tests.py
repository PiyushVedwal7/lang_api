from django.test import TestCase
from .models import FAQ

class FAQTests(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="Test Question", answer="Test Answer")
        self.assertEqual(faq.get_translated_question('en'), "Test Question")