from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models import Post

# NOTE: admin権限は利用想定していないのでテストしない
# TODO: user権限でログイン可能になったらテストケース追加する

class TestListView(TestCase):
    fixtures = ["tests/users.yaml"]
    post_new_url = reverse("post_new")
    post_list_url = reverse("post_list")

    def staff_login(self):
        self.client.logout()
        self.client.force_login(User.objects.get(username="staff"))

    # ---------------------- test ----------------------

    def test_正常系_ページ遷移(self):
        self.staff_login()
        response = self.client.get(self.post_new_url)
        self.assertEqual(response.status_code, 200)

    def test_正常系_データPOST(self):
        self.staff_login()
        params = {"title": "タイトル１", "text": "内容１"}

        self.assertEqual(Post.objects.all().count(), 0) # 初期状態では何も登録されていないことを確認

        create_response = self.client.post(self.post_new_url, params)
        self.assertEqual(create_response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="タイトル１").exists())

    def test_正常系_title200文字(self):
        self.staff_login()
        params = {
            "title": "t" * 200,
            "text": "内容",
        }
        # データの登録
        create_response = self.client.post(self.post_new_url, params)
        self.assertEqual(create_response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="t" * 200).exists())

    def test_異常系_タイトルなし(self):
        self.staff_login()
        params = {
            "title": "",
            "text": "内容のみ_タイトルなし",
        }
        # データの登録
        create_response = self.client.post(self.post_new_url, params)
        self.assertNotEqual(create_response.status_code, 302)
        expect_form_errors = {"title": ["このフィールドは必須です。"]}
        self.assertDictEqual(create_response.context["form"].errors, expect_form_errors)
        # データが登録されていないことを確認
        self.assertFalse(Post.objects.filter(text="内容のみ_タイトルなし").exists())

    def test_異常系_内容なし(self):
        self.staff_login()
        params = {
            "title": "タイトルのみ_内容なし",
            "text": "",
        }
        # データの登録
        create_response = self.client.post(self.post_new_url, params)
        self.assertNotEqual(create_response.status_code, 302)
        expect_form_errors = {"text": ["このフィールドは必須です。"]}
        self.assertDictEqual(create_response.context["form"].errors, expect_form_errors)
        # データが登録されていないことを確認
        self.assertFalse(Post.objects.filter(title="タイトルのみ_内容なし").exists())

    def test_異常系_title201文字(self):
        self.staff_login()
        params = {
            "title": "t" * 201,
            "text": "内容",
        }
        # データの登録
        create_response = self.client.post(self.post_new_url, params)
        self.assertNotEqual(create_response.status_code, 302)
        expect_form_errors = {"title": ["この値は 200 文字以下でなければなりません( 201 文字になっています)。"]}
        self.assertDictEqual(create_response.context["form"].errors, expect_form_errors)
        # データが登録されていないことを確認
        self.assertFalse(Post.objects.filter(text="内容").exists())