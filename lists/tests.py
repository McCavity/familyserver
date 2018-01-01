from django.test import TestCase

# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_lists_home_template(self):
        response = self.client.get('/lists/')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/lists/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
