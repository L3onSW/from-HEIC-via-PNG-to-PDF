# from HEIC via PNG to PDF
複数枚のHEIC形式の画像をファイル名はそのままでPNGに変換し、その後1つのPDFファイルに変換する

## 🚨 注意点
- 画像枚数が多いとローカルPCのメモリ容量が「Killed: 9 (システムによってプロセスが強制終了)」となる場合があります。

## 💻 実行環境
スクリプト作成者は以下の環境で実行しました。
- macOS 13.4.1
- Python 3.9.6

## 🧑‍💻 実行方法
### 実行手順1. HEICからPNGへの変換
[01_from-HEIC-to-PNG.py](01_from-HEIC-to-PNG.py)の以下の部分を適切なディレクトリに書き換えます。
```python
indir = './00_HEIC-Images'
outdir = './01_PNG-Images'
```
[01_from-HEIC-to-PNG.py](01_from-HEIC-to-PNG.py)を以下のように実行します。
```console
$ python 01_from-HEIC-to-PNG.py
```
### 実行手順2. PNGからPDFへの変換
[02_from-PNG-to-PDF.py](02_from-PNG-to-PDF.py)の以下の部分を適切なディレクトリに書き換えます。
```python
indir = './01_PNG-Images'
outpdf = './02_PDF/output.pdf'
```
[02_from-PNG-to-PDF.py](02_from-PNG-to-PDF.py)を以下のように実行します。
```console
$ python 02_from-PNG-to-PDF.py
```

## 📚 参考文献
1. [PyPI. "pyheif 0.8.0". (参照:2024-09-16).](https://pypi.org/project/pyheif/)
2. [PyPI. "pillow 10.4.0". (参照:2024-09-16).](https://pypi.org/project/pillow/)
3. [PyPI. "psutil 6.0.0". (参照:2024-09-16).](https://pypi.org/project/psutil/)
