# scripts/inspect_data.py
"""Inspect the Kolipakam DravLex data structure."""

import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw/2018_02_26_lingpy_analyses_for_RSOS_SI_ SI_robustness_cognate_coding")

def inspect_files():
    """Check what's in each file."""
    
    # 1. Check the main CSV file
    print("=" * 60)
    print("DravLex-2017-04-23.csv")
    print("=" * 60)
    df_csv = pd.read_csv(RAW_DIR / "DravLex-2017-04-23.csv")
    print(f"Shape: {df_csv.shape}")
    print(f"\nColumns: {df_csv.columns.tolist()}")
    print(f"\nFirst few rows:")
    print(df_csv.head())
    print(f"\nLanguages: {df_csv['DOCULECT'].unique() if 'DOCULECT' in df_csv.columns else 'Check column name'}")
    
    # 2. Check the TSV file (might be LingPy format)
    print("\n" + "=" * 60)
    print("DravLex.tsv")
    print("=" * 60)
    df_tsv = pd.read_csv(RAW_DIR / "DravLex.tsv", sep="\t")
    print(f"Shape: {df_tsv.shape}")
    print(f"\nColumns: {df_tsv.columns.tolist()}")
    print(f"\nFirst few rows:")
    print(df_tsv.head(10))
    
    # 3. Check languages file
    print("\n" + "=" * 60)
    print("languages.csv")
    print("=" * 60)
    langs = pd.read_csv(RAW_DIR / "languages.csv")
    print(langs)
    
    # 4. Check concepts
    print("\n" + "=" * 60)
    print("concepts.tsv")
    print("=" * 60)
    concepts = pd.read_csv(RAW_DIR / "concepts.tsv", sep="\t")
    print(f"Total concepts: {len(concepts)}")
    print(concepts.head(20))
    
    return df_csv, df_tsv, langs, concepts

if __name__ == "__main__":
    inspect_files()
