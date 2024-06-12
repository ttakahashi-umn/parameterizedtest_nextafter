# parameterizedtest_nextafter

pytestにおけるparametrize(パラメータ化)とnextafterによる境界値試験

## はじめに

このリポジトリではパッケージマネージャーにryeを用いています。
ryeのインストール方法についてはこちらをご覧ください。

[今巷で話題のRyeについて調べてみた](https://qiita.com/hiseumn/items/5baa2eb44885dffc9bac)

## ライブラリのインストールについて

次の手順で必要なライブラリをインストールすることができます。

### ryeがあるかた

```terminal
rye sync
```

### ryeがないかた

```terminal
pip install -r requirements-dev.lock
```

## プログラムの実行方法

以下のコマンドを実行してください。

```terminal
pytest src/parameterizedtest_nextafter/main.py
```

以上
