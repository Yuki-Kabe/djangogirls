# 役割
ログイン用のテンプレート

## 実装のメモ
- form.errors : Djangoがフォームの内容を精査してエラーの場合に表示する内容
- ログインはPOSTメソッドで行う
- ここではDjangoフォームを活用(LoginView)
    - {{ form.username.label_tag }} : `ユーザ名:`というラベルHTMLを自動生成
    - {{ form.username }} : <input type="text" name="username" ...>を自動生成
    - {{ form.password.label_tag }} : `パスワード:`というラベルHTMLを自動生成
    - {{ form.password }} : <input type="password" name="password" ...>を自動生成
- <input type="submit" value="login"/> : ログインボタン
- <input type="hidden" name="next" value="{{ next }}" /> : {{ next }}はログイン後のリダイレクト先を示す(プロジェクトの`urls.py`で指定している。)