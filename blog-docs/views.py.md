# 役割
リクエストを受け取り、必要なデータを取得(Modelの選択)、レスポンスの加工/レンダリング(Templateの選択)を行う。MVCでいうとController的な役割

ここでメソッドを定義して`urls.py`で参照して適宜呼び出す

## メソッドの引数
基本的にrequestのみでOKだが、パスパラメータなどを用いたい場合は第二引数を用意。その際は`urls.py`で指定する変数名と同じもので引数を定義しないとエラーになる。

## render()メソッド
PythonのデータをHTMLテンプレートに埋め込んでブラウザに返すための関数
```
render(request, template_name, context=None, content_type=None, status=None, using=None)
```
- request : HttpRequestオブジェクト。これはimportしなくても勝手にDjangoがいい感じにしてくれてるっぽい
- template_name : 利用したいテンプレートファイル(ページのファイルパス)
- context : テンプレートで使用するデータ(辞書形式。キーはテンプレートでデータアクセスする際に利用する)

## redirect()メソッド
処理が終わったあとに別のページなどに自動遷移したい際に利用する
```
render(URL名, 引数があれば指定。なければ第1引数のURL名だけで良い)
```

## post_new()について
`base.html`から呼ばれるときは`request.method="GET"`なのでelseを表示する。<br>
フォームに値を入力して送信ボタンを押した際は`request.method="POST"`なのでFormクラスに設定されているModelをsave()してそのデータの詳細画面にリダイレクトする。

## post_edit()について
処理概要
1. パスパラメータのpkでpostの情報を取得できるか確認。できない場合は404
2. request.method="POST"であればFormクラスの設定されているModelをsave()して再度ページを更新
3. request.method="GET"であれば(`post_detail.html`から呼び出された時)1.で取得したデータの情報をフォームに詰めてページを描画


## 実装のメモ
- `post_detail(request, pk)` : `urls.py`で定義した`pk`を引数にとる。(全く同じ変数名にしないとエラーになるので注意)
- `get_object_or_404(モデル名, 条件)` : Noneの場合、404のページにリダイレクトさせる