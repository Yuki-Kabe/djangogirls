# 役割
リクエストを受け取り、必要なデータを取得(Modelの選択)、レスポンスの加工/レンダリング(Templateの選択)を行う。MVCでいうとController的な役割

ここでメソッドを定義して`urls.py`で参照して適宜呼び出す

### render()メソッド
PythonのデータをHTMLテンプレートに埋め込んでブラウザに返すための関数
```
render(request, template_name, context=None, content_type=None, status=None, using=None)
```
- request : HttpRequestオブジェクト。これはimportしなくても勝手にDjangoがいい感じにしてくれてるっぽい
- template_name : データを渡すテンプレートファイル
- context : テンプレートに渡すデータ(辞書形式)