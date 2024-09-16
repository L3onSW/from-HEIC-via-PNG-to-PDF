# ======================================================================
# 02_from-PNG-to-PDF.py
# 複数枚のPNG画像を1つのPDFファイルに変換する
#
# Created on 2024/09/16, author: L3onSW
# ======================================================================

import os
from PIL import Image
import psutil
import time

indir = './01_PNG-Images'
outpdf = './02_PDF/output.pdf'


# メモリ使用量を表示する関数
def print_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    # メモリ使用量 (MB)
    print(f"メモリ使用量: {mem_info.rss / 1024 / 1024:.2f} MB")


# PNGファイルのリストを取得し、昇順にソート
pngs = sorted([f for f in os.listdir(indir) if f.lower().endswith('.png')])
# PNGファイルが存在しない場合のエラーメッセージ
if not pngs:
    print("指定されたディレクトリにPNGファイルが見つかりません。")
    exit()
# 画像を開いて、リストに追加
image_list = []
for idx, file in enumerate(pngs):
    file_path = os.path.join(indir, file)
    try:
        # PNGはRGBA形式なのでRGBに変換
        img = Image.open(file_path).convert('RGB')
        image_list.append(img)
        print(f"{file} を処理中...")
        # メモリ使用量を表示
        print_memory_usage()
        # 短い遅延を追加してメモリ使用量を確認しやすくする
        time.sleep(1)
    except Exception as e:
        print(f"{file}を開くことができませんでした: {e}")

# 最初の画像を基にPDFを作成し、他の画像を追加
if image_list:
    first_image = image_list[0]
    other_images = image_list[1:]
    first_image.save(outpdf, save_all=True, append_images=other_images)
    print(f"PDFファイルが正常に生成されました: {outpdf}")
else:
    print("有効なPNGファイルがありません。")
