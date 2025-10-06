# 役割
base.htmlに差し込む情報をこちらに記述する。<br>
投稿の詳細ページ

## Djangoのテンプレート構文
Djangoの機能を利用する場合は{% %}のような形で書く。
- `{% load static %}` : staticディレクトリの読み込み
- `{% block content %}` : `content`というブロックを作成する
- `{% extends 'アプリ名/base.html' %}` : `アプリ名/base.html` を読み込んで拡張する。
- `{% url 'urls.pyで定義したURLパターン名' URLのメソッドに渡す値 %}`

## 要素の差し込み(ファイル分割)
親ファイルで宣言された`{% block ブロック名 %}`の中身をextendsしたこちらのファイルで記述する。

## viewから渡されたデータの参照
viewからは辞書形式でデータを渡されるのでそのキーでアクセスできる。その際キーを`{{}}`で括る

## 実装のメモ
- {% if文 %} : {% endif %}を忘れずに
- glyphicon glyphicon-pencil : Boostrap3に含まれているアイコンフォント。鉛筆マーク。spanタグで囲む必要あり
