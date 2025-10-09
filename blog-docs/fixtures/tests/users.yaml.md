# 役割
テスト用のuser定義ファイル

テストファイルに以下のように記述して読み込む
```
class TestExample(TestCase):
    fixtures = ["tests/users.yaml"]
```