# 役割
base.htmlに差し込む情報をこちらに記述する。<br>
formを用いてコメントの新規作成を行うページ

## {{ form.as_p }}
Djangoフォームの核の部分<br>
作成したフォームクラス(modelの情報とfieldsに指定した要素など)を読み取って、HTMLタグで自動描画する。<br>
`as_p`はpタグで囲って表示するというメソッド

## 実装のメモ
- formタグ : ブラウザでデータを送るためのHTMLフォーム
- method : データ送信方式(POST,GETなどがある)
- class="post-form" : blog.cssで定義している
- {% csrf_token %} : CSRF攻撃を防ぐためのセキュリティ対策タグ。Djangoが自動で安全なトークンを発行して、POST送信時に検証する。<b>必ずフォームの中に書く必要がある。</b>
- buttonタグ,type="submit" : 押すとフォームが送信される
- saveクラス : blog.cssで定義している
- btn btn-default : Bootstrapのボタンデザインクラス