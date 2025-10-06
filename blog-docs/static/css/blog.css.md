h1 a : CSSセレクタと呼ばれる。h1要素内のa要素にすているを適用することを意味している。`,`で複数セレクタに同じ設定の適応が可能

font-family: 'Lobster';はhtml側でgoogleフォントを読み込む必要がある。このファイルの前にimpoprtしておくこと。
```
<link href="//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```

`.`ではじまるセレクタはクラスに関連する。