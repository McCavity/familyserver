from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_lists_index_template(self):
        response = self.client.get('/lists/')
        self.assertTemplateUsed(response, 'lists/home.html')
