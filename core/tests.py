from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from core.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Halfpap Family Server</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
