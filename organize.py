import os
import shutil
import pandas as pd
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

df = pd.read_csv('tickers.csv')
valid_tickers = set(df['ticker'].astype(str).str.upper())

files = os.listdir(base_dir)

ticker_pattern = re.compile(r'^([A-Z0-9]+)(\s+[A-Z]+)?')

for file in files:
    if not file.lower().endswith(('.xlsx', '.xls')) or os.path.isdir(file):
        continue

    match = ticker_pattern.match(file)
    if not match:
        continue

    ticker = match.group(1).upper()
    if ticker not in valid_tickers:
        continue

    folder_path = os.path.join(base_dir, ticker)
    os.makedirs(folder_path, exist_ok=True)

    src = os.path.join(base_dir, file)
    dest = os.path.join(folder_path, file)
    if os.path.abspath(src) != os.path.abspath(dest):
        shutil.move(src, dest)
        print(f"Moved {file} → {ticker}/")

print("Done organizing Excel files.")
