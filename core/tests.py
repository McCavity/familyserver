from django.test import TestCase

from core.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_core_index_template(self):
        response = self.client.get('/')  
        self.assertTemplateUsed(response, 'core/index.html')
