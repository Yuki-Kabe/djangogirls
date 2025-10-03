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