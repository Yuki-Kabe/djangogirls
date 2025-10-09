# 役割
DBへ読み込む初期データ（シリアライズ済み）を置く。<br>
主にユーザの初期データなどを`.json`ファイルや`.yaml`ファイルで記述する。

## データ読み込み
以下のコマンドでデータを読み込む
```
python3 manage.py loaddata <モデル名>

ex. users.yamlを読み込む
python3 manage.py loaddata users
```

## データダンプ
現在のDBデータをdumpすることもできる
```
python3 manage.py dumpdata auth.user --format=yaml --indent 2 > blog/fixtures/users.yaml
```

## ユーザー追加
認証ユーザーを追加するときは`ハッシュ化済みパスワード`を置く必要がある（平文は不可）。
簡単なハッシュ化済みパスワードを入手する方法は例えば以下
```
python3 manage.py shell
from django.contrib.auth.hashers import make_password
make_password("<パスワード>") # ハッシュ化されたパスワードが表示されるのでそれを記述
```

