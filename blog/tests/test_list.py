from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# TODO : user権限でログイン可能になったらテストケースを追加する

class TestListView(TestCase):

    fixtures = ['tests/users.yaml']
    list_url = reverse('post_list')

    def admin_login(self):
        self.client.logout()
        self.client.force_login(User.objects.get(username="dev"))

    def staff_login(self):
        self.client.logout()
        self.client.force_login(User.objects.get(username="staff"))

    # ---------------------- test ----------------------

    def test_正常系_admin権限_記事一覧(self):
        self.admin_login()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_正常系_staff権限_記事一覧(self):
        self.staff_login()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_正常系_未ログイン(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)