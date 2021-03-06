from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    # setUp()は、各テストメソッドの最初に実行される
    def setUp(self):
        self.Client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@gmail.com",
            password="password123"
        )   

        # 管理画面に入れるユーザーを作成して、管理画面にログインする。
        # もし、以下のコードがなければ、テストを実行した時に、管理画面に
        # ログインできず、302リダイレクトエラーが発生する
        self.Client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email="test@gmail.com",
            password="password123"
        
        )

    def test_users_listed(self):
        # 管理画面のユーザーリストページを表示 url =reverse('admin:core_user_changelist')
        # ※上記のやり方が正しいことやり方だが、今回は直接呼び出す
        res = self.Client.get(f'http://localhost/admin/yorozu/account/')
        
        self.assertContains(res,self.user.email)
        # # 以下のものは、上記のself.assertContains(res,self.user.email)と同じ
        # self.assertContains(res,"test@gmail.com")


    # =======================================================================================
    # self.assertTemplateUsed(res, 'template_name'): レスポンスがテンプレートを使っているかテスト
    # self.assertContains(res, '文字列'): レスポンスを描画した結果 '文字列' を含むかテスト
    # 表示されるhtmlのソースコードの中に"文字列"という言葉があるか判断する
    # =======================================================================================


    # =======================================================================================
    # res = self.Client.get(f'http://localhost/admin/yorozu/account/')の中身
    # res.contextという形で中身を確認できる
    # =======================================================================================


    def test_user_change_page(self):
        """データを編集できるページに遷移できるかテストする"""

        res = self.Client.get(f'http://localhost/admin/yorozu/account/{self.user.id}/change/')
        self.assertEqual(res.status_code, 200)


    def test_create_user_page(self):
        """アカウントの追加ページに遷移できるか"""
        res = self.Client.get("http://localhost/admin/yorozu/account/add/")
        self.assertEqual(res.status_code, 200)
