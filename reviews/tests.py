from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from books.models import Book
from .models import Review
from .views import ReviewCreateView


class ReviewTest(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='review.user@email.com',
            password='testpass123'
        )
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00'
        )
        self.review = Review.objects.create(
            book=self.book,
            title='A nice book',
            type='POS',
            review='A very nice book. Enjoyed it.',
            author=self.user
        )

    def test_book(self):
        self.assertEqual(self.book.title, 'Harry Potter')
        self.assertEqual(self.book.author, 'JK Rowling')
        self.assertEqual(self.book.price, '25.00')

    def test_review(self):
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.title, 'A nice book')
        self.assertEqual(self.review.type, 'POS')
        self.assertEqual(self.review.review, 'A very nice book. Enjoyed it.')
        self.assertEqual(self.review.author, self.user)

    def test_create_review_view(self):
        """
        In this test we login a user and then call create review url
        follow is set to true so that we follow the redirection for
        authentication.
        using force_login  will login the user without us having to
        worry about password or anything. If login is used the test will fail
        """
        self.client.force_login(self.user)
        response = self.client.get(reverse('review_create'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_create_form.html')
        self.assertContains(response, 'Write Review')
        self.assertNotContains(response, 'Hello world')
        response = self.client.post(reverse('review_create'), {
            'title': 'abc',
            'review': 'def',
            'type': 'POS',
            'book': self.book
        },
                                    follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_review_url_resolves_review_create_view(self):
        view = resolve('/reviews/create/')
        self.assertEqual(
            view.func.__name__,
            ReviewCreateView.as_view().__name__
        )

    def test_review_update_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.review.get_absolute_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/review_update_form.html')
        self.assertContains(response, 'Update Review')
        self.assertContains(response, 'A nice book')
        response = self.client.post(self.review.get_absolute_url(),
                                    {
                                        'title': 'A bad book'
                                    },
                                    follow=True)
        # response = self.client.get(self.review.get_absolute_url(), follow=True)
        self.assertEqual(response.status_code, 200)
        review = Review.objects.all()
        print(review)


class LoginRequiredCreateReviewView(TestCase):
    """
    A class to test that anonymous user is
    redirected to login page when creating a review
    """

    def test_redirection(self):
        url = reverse('review_create')
        login_url = reverse('account_login')
        response = self.client.get(url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=url))
