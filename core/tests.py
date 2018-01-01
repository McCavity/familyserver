from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_core_index_template(self):
        response = self.client.get('/')  
        self.assertTemplateUsed(response, 'core/index.html')
