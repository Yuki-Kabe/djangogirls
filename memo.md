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
https://tutorial.djangogirls.org/ja
## Djangoのinstall
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

## プロジェクトを作成しよう！
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