# ======================================================================
# 01_from-HEIC-to-PNG.py
# 複数枚のHEIC画像を同じファイル名の複数枚のPNG画像に変換する
#
# Created on 2024/09/16, author: L3onSW
# ======================================================================

import os
from PIL import Image
import pyheif
import psutil
import time

indir = './00_HEIC-Images'
outdir = './01_PNG-Images'


# メモリ使用量を表示する関数
def print_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    print(f"メモリ使用量: {mem_info.rss / 1024 / 1024:.2f} MB")


# HEICファイルをPNGに変換する関数
def convert_heic_to_png(inpath, outpath):
    heif_file = pyheif.read(inpath)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(outpath, "PNG")


# 指定ディレクトリ内のHEICファイルを昇順で処理
heics = sorted([f for f in os.listdir(indir) if f.lower().endswith('.heic')])
# HEICファイルが存在しない場合のエラーメッセージ
if not heics:
    print("指定されたディレクトリにHEICファイルが見つかりません。")
    exit()
# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(outdir):
    os.makedirs(outdir)
# HEIC1枚ずつをPNG1枚ずつに変換していく
for fname in heics:
    inpath = os.path.join(indir, fname)
    outpath = os.path.join(outdir, fname.replace('.HEIC', '.png'))
    try:
        convert_heic_to_png(inpath, outpath)
        print(f"変換しました: {fname} -> {outpath}")
        # 変換後にメモリ使用量を表示
        print_memory_usage()
        # メモリの状態を確認しやすくするために1秒の遅延
        time.sleep(1)
    except Exception as e:
        print(f"[Error] 変換に失敗しました {fname}: {e}")
