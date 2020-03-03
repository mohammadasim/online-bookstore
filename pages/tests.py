from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class HomepageTests(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, 'Home page')

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hello world')

    def test_home_page_url_resolves_homepageview(self):
        """
        Checks that the name of the view used to resolve
        url '/' matches HomePageView
        """
        view = resolve('/')
        self.assertEqual(view.func.__name__,
                         HomePageView.as_view().__name__)
