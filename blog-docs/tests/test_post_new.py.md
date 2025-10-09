# 役割
テストファイル

unittestを利用しているらしい。Pytestを利用しようとするとDB周りの接続とかの設定が結構ややこしいらしい。

## テストの実行
```
# プロジェクトのテストを全実行
python3 manage.py test

# アプリケーションのテストを全実行
python3 manage.py test <アプリ名>

# アプリケーションのファイルを指定して実行(__init__.pyをtestsディレクトリ配下に置いておく必要あり)
python3 manage.py test <アプリ名>.tests.<ファイル名>
```

## 実装のメモ
- fixtures : 初期DBのデータを記述するファイル
- reverse() : urls.pyで定義しているURL名からURLを逆引きする関数

