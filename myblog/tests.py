from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post
from myblog.models import Category
import datetime
from django.utils.timezone import utc

"""

Usage:
python manage.py test myblog
python manage.py test myblog.tests.CategoryTestCase.test_string_representation
python manage.py test myblog.tests.FrontEndTestCase.test_list_only_published

./manage.py test

"""
class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)

class FrontEndTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json',]

    def setUp(self):
        self.now = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            title = "Post %d Title" % count
            # print("NEXT TITLE:", title)
            post = Post(title="Post %d Title" % count,
                text="foo",
                author=author)
            if count < 6:
                # print("setting published date") # create 5 records with a published date
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate 
            post.save()



    def test_list_only_published(self):

        # print("Xxxx x x x x x x test_list_only_published  x xx x x ")
        resp = self.client.get('/')
        # the content of the rendered response is always a bytestring
        resp_text = resp.content.decode(resp.charset)
        # print(resp_text)
        self.assertTrue("Recent Posts" in resp_text)
        for count in range(1, 11):
            title = "Post %d Title" % count
            if count < 6:
                self.assertContains(resp, title, count=1)
            else:
                self.assertNotContains(resp, title)

    def test_details_only_published(self):
        for count in range(1, 11):
            title = "Post %d Title" % count
            # print("title", title)
            post = Post.objects.get(title=title)
            resp = self.client.get('/posts/%d/' % post.pk)
            if count < 6:
                self.assertEqual(resp.status_code, 200)
                self.assertContains(resp, title)
            else:
                self.assertEqual(resp.status_code, 404)

