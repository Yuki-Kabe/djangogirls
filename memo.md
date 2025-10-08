# 環境構築
https://tutorial.djangogirls.org/ja/python_introduction/
が開始できる状態にする。加えてデバッガーが使用できるようにしておく。
## 1. Dockerコンテナの作成
1. リポジトリをクローンする
2. 以下を実行
```
cd djangogirls
docker compose up -d
```
## 2. VSCode(ホストPC)の設定
1. 拡張機能 [DevContainers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) をinstall

## 3. コンテナの設定
1. コンテナを起動したら`Visual Studio Code をアタッチする`でコンテナにアタッチ
2. pythonのversionが3.11であることを確認(`python3 --version`で確認)
3. pipがpython3.11のものであることを確認(`pip --version`で確認)
4. コンテナにVSCodeの拡張機能 [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) をinstall

## 4. 必要なpackageのisntallなど権限周りでできない場合
apt-get install などdevアカウントでは権限の関係でinstallできない
ホストのOSから以下でrootユーザーでコンテナにアクセスして操作する
```
docker exec -uroot -it <コンテナ名> bash
ex.) docker exec -uroot -it django-girls-web bash
```

# DjangoGirls
https://tutorial.djangogirls.org/ja を進めていく。各ページごとにコミットする。環境構築が完了していればDjangoのインストールから開始できるはず。
## [Djangoのインストール](https://tutorial.djangogirls.org/ja/django_installation/)
1. `dockerfile`などと同じディレクトリの位置に`requirements.txt`を作成して資料通りにinstall
2. install時に以下のwarningが出たらpathを通す(`~/.bashrc`などに`export PATH=$HOME/.local/bin:$PATH`を追記)
```
Installing collected packages: sqlparse, asgiref, Django
  WARNING: The script sqlformat is installed in '/home/dev/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━━━━━━━━━━ 2/3 [Django]  WARNING: The script django-admin is installed in '/home/dev/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Django-5.1.13 asgiref-3.9.2 sqlparse-0.5.3
```
3. bashを再起動して`django-admin`コマンドが利用できるか確認

## [プロジェクトを作成しよう！](https://tutorial.djangogirls.org/ja/django_start_project/)
`python3 manage.py runserver 0.0.0.0:8080`を実行
```
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/zoneinfo/_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key Asia/Tokyo'
```
tzdataというパッケージのinstallが必要らしい。`apt-get install tzdata`した。

再度`python3 manage.py runserver 0.0.0.0:8080`を実行
http://localhost:8080/ でアクセスした。成功

## [Djangoモデル](https://tutorial.djangogirls.org/ja/django_models/)
新しく`blog`というアプリケーションを作成する。プロジェクトとアプリケーションの違いがよくわからない。mysiteとblogの違いは何なのだろうか。<br>
`mysite/settings.py`に新しく作成した`blogアプリ`を追加する。

blogアプリのデータモデルを設計する。blog/models.pyに記述。<br>

マイグレーション実行。<br>
```
python3 manage.py makemigrations <アプリ名> # マイグレーションファイルを作成。
# アプリ名/migrations配下にマイグレーションファイルが作成される

# アプリ名/migrations配下にマイグレーションファイルがあることを確認してマイグレ実行
python3 manage.py migrate <アプリ名> # マイグレーション実行
```

## [ログインページを作ろう (Django admin)](https://tutorial.djangogirls.org/ja/django_admin/)
前の章で作成したポストのデータをCRUDするのにadmin管理画面を作成する。

スーパーユーザ(サイトの全ての権限を持つユーザ)を作成<br>
```
python3 manage.py createsuperuser
```
- ユーザ名 : dev
- メールアドレス : dev@example.com
- パスワード : devPassword
で作成

serverを立ち上げ`python3 manage.py runserver 0.0.0.0:8080`、http://localhost:8080/admin にアクセス。設定したユーザ名とパスワードでログイン

管理画面上から記事を3つ作成した。

## [デプロイ](https://tutorial.djangogirls.org/ja/deploy/)
pythonanywhereにデプロイする。(以前はherokuだったらしいが有料化したため無料のpythonanywhereになった)

pythonanywhereでアカウント作成(bekar28)、APIトークンを発行、Dashboardの画面からbashを起動<br>
```
pip install --user pythonanywhere
pa_autoconfigure_django.py --python=3.13 https://github.com/Yuki-Kabe/djangogirls.git --nuke # 3.6だとエラーになったのでpythonanywhereのデフォルトの3.13にした
python3 manage.py createsuperuser
ユーザー名 (leave blank to use 'bekar28'):
メールアドレス: gmailのやつ
Password: 設定した
Superuser created successfully.
```
https://ユーザ名.pythonanywhere.com/ でアクセス。https://ユーザ名.pythonanywhere.com/

## [Django URL](https://tutorial.djangogirls.org/ja/django_urls/)
アプリケーションのディレクトリに`urls.pyファイル`を新規作成し、プロジェクトの`urls.pyファイル`でimportした。<br>
この章はviewの設定をしていないのでserverを動かそうとするとエラーになるが問題なし。

## [Djangoビュー](https://tutorial.djangogirls.org/ja/django_views/)
アプリケーションのviews.pyを編集。テンプレートが存在しないのでこの章でも動かないが問題なし。

## [HTML入門](https://tutorial.djangogirls.org/ja/html/)
アプリケーションのviews.pyが参照するテンプレートファイルを作成した。このとき、アプリケーションのディレクトリ配下に`templates/アプリ名`でディレクトリを作って、その配下にテンプレートファイルを配置した。こうすると何かと都合が良いらしい。

## [Django ORM (クエリセット)](https://tutorial.djangogirls.org/ja/django_orm/)
DjangoのインタラクティブコンソールでORMを利用してみる
```
python3 manage.py shell
```
コンソールからはアプリケーションのmodels.pyをimportして`モデル名.objects.メソッド`でcrudできる
ex)
```
from blog.models import Post # Postオブジェクトをimport
# 全てget
Post.objects.all()
# フィルターしてget
Post.objects.filter(title__contains='test') # プロパティ__メソッドというように"__"で繋ぐ

# Create
from django.contrib.auth.models import User # Userオブジェクトをimport
me = User.objects.get(username='dev')
Post.objects.create(author=me, title='Sample title', text='Create Test')

# Postオブジェクトで定義したメソッドを利用(published_dateがnullなのでpublish()で現在時刻に設定)
post = Post.objects.get(title='Sample title')
post.publish()

# メソッドチェーン
from djnago.utils impot timezone
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
```

## [テンプレート内の動的データ](https://tutorial.djangogirls.org/ja/dynamic_data_in_templates/)
DjangoではViewがController的な役割をする。<br>
Viewのrender()関数では読み込むテンプレートファイルと描画に必要なデータを指定して、それを元にページをレンダリングする。
アプリケーションの`views.py`を編集してmodelからテンプレートへデータを渡した。

## [Djangoテンプレート](https://tutorial.djangogirls.org/ja/django_templates/)
Viewからもらったデータを用いて動的にページが表示できるようにした。

## [CSSでカワイくしよう](https://tutorial.djangogirls.org/ja/css/)
CSSでページの装飾。bootstrapも利用<br>
アプリケーション/static/ディレクトリを作成してテンプレートファイルで`{% load static %}`を記述するとDjangoが自動的にディレクトリを検索して読み込んでくれる。具体的にどのファイルを読み込むかはさらにhead要素で指定する。

 ## [テンプレートを拡張しよう](https://tutorial.djangogirls.org/ja/template_extending/)
 post_list.htmlに全ての記述を行なってたが、全ページで共通になりそうな部分をbase.htmlに切り出して、post_list.htmlはそれを読み込む形にした。

 ## [アプリケーションを拡張しよう](https://tutorial.djangogirls.org/ja/extend_your_application/)
 テンプレートの遷移先リンクを設定する。<br>
 1. アプリケーション側の`urls.py`で新しいURLパターンを定義
 2. `views.py`でURLパターンで呼び出されるメソッドを定義
 3. 遷移先のテンプレートを作成
 4. 遷移元のテンプレートのhref属性に定義したURLを指定。渡す値の設定なども

PythonAnywhere<br>
コンソールからリポジトリをpullして、CSSの更新を行う。
```
cd ~/<your-pythonanywhere-domain>.pythonanywhere.com
python3 manage.py collectstatic
```
Reloadしてコードが反映されたことを確認する

## [Djangoフォーム](https://tutorial.djangogirls.org/ja/django_forms/)
フォームを作成する。<br>
DjangoフォームはFormクラスが保存対象とするModelクラスの必須項目などの情報を読み取ってPOST時に値が正しいのか自動で検証してくれる。(基本的なバリデーションは書く必要なし)

新規作成<br>
アプリケーションの`forms.pyファイル`を新規作成<br>
- フォームを送信するためのページ`post_edit.html`テンプレートを新規作成
- `views.py`にフォーム画面を描画/フォームの内容を保存するためのメソッド(`post_new`)を作成
- `urls.py`に作成したviewのメソッドのURLパターンを追加
- `base.html`に作成したviewのメソッドを呼び出すリンクを追加(新規作成フォーム画面に遷移する)

既存の更新<br>
- `views.py`にフォーム画面を描画/フォームの内容を保存するためのメソッド(`post_edit`)を作成
- `urls.py`に作成したviewのメソッドのURLパターンを追加
- `post_detail.html`に作成したviewのメソッドを呼び出すリンクを追加(編集フォーム画面に遷移する)

認証の追加
フォームページに遷移するのに{% user.is_authenticated %}でログインしているユーザーのみ新規作成できるように修正。シークレットモードで＋マークが消えていることを確認。

## [ウェブサイトにもっと機能を追加しよう](https://tutorial-extensions.djangogirls.org/ja/homework/)
draft一覧ページ作成
- `post_draft.html`テンプレートを作成
- `views.py`にdraft用のページを描画するためのメソッドを新規作成
- `urls.py`に新規作成したviewのメソッドのURLパターンを追加
- `base.html`に新規作成したviewのメソッドを呼び出すリンクを追加(ドラフト画面に遷移する)

publish機能追加
- `views.py`にpublish用のメソッドを新規作成
- `urls.py`に新規作成したviewのメソッドのURLパターンを追加
- `post_detail.html`にviewメソッドを呼び出すボタンを追加

delete機能追加
- `views.py`にdelete用のメソッドを新規作成
- `urls.py`に新規作成したviewのメソッドのURLパターンを追加
- `post_detail.html`にviewメソッドを呼び出すボタンを追加

## [ウェブサイトをセキュアにする](https://tutorial-extensions.djangogirls.org/ja/authentication_authorization/)
デコレータを用いて書くメソッドの実行をログイン必須にする。<br>
Djangoにはログインのための承認ツールが既に用意されている`django.contrib.auth`

- プロジェクトの`urls.py`にloginのURLパターンを設定
- `views.py`の各メソッドに`@login_required`を記述
- アプリケーションのtemplates配下に`registration/login.html`を新規作成
- プロジェクトの`settings.py`にLOGIN_REDIRECT_URLの設定の記述を追加

- Django5.1以降はログアウト時にもPOSTメソッドを利用しないといけないらしく、サイトの通りに書くとログアウトメソッドを呼び出して405エラーになる。

## [コメントモデルを作ろう](https://tutorial-extensions.djangogirls.org/ja/homework_create_more_models/)
データモデルを拡張する。<br>

`Comment`クラスの定義
- アプリケーションの`models.py`に新しい`Comment`classを追加する
マイグレーション実行
```
python3 manage.py makemigrations <アプリ名>
python3 manage.py migrate <アプリ名>
```
- アプリケーションの`admin.py`に新しく作成した`Comment`classを追加する
- `post_detail.html`にpostに紐づくcommentを全て表示するように記述を追加
- `post_list.html`にpostに紐づくコメント数を表示するように修正

`Comment`クラスのフォーム追加
- `forms.py`に`CommentForm`クラスを実装
- `add_comment_to_post.html`テンプレートを新規作成(フォーム用の画面)
- `views.py`にフォーム画面を描画/フォームの内容を保存するためのメソッド(`add_comment_to_post`)を作成
- `urls.py`に作成したメソッドを追加
- `post_detail.html`に追加したviewメソッドを呼び出すボタンを追加

`Comment`のapprove,remove
- `post_detail.html`に非ログイン者にはapproveされたコメントのみが見えるようにif分岐を追加
- `views.py`にapprove用メソッド、remove用メソッドを追加
- `urls.py`に追加したメソッドのURL名を定義
- `post_detail.html`にログイン者のみが利用可能なapproveされていないcommentのremove,approveメソッドに関するボタンを追加
- `models.py`の`Post`クラスに紐づいているapprove済みのリレーションの一覧を取得するようなメソッドを定義
- `post_list.html`の部分を定義したメソッドを利用してcountするように修正