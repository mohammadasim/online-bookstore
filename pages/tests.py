from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    """ Test class for HomePage """

    def setUp(self) -> None:
        url = reverse('pages:home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, 'Contact Us')

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


class AboutPageTests(SimpleTestCase):
    """ Test class for About Page """

    def setUp(self) -> None:
        url = reverse('pages:about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About us')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hello world')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
