# scripts/fix_data_format.py
"""Fix data format for BEASTling - needs wide format with languages as rows."""

import pandas as pd
from pathlib import Path

def check_current_formats():
    """Check what we have in both files."""
    
    print("=" * 60)
    print("LONG FORMAT (current - WRONG for BEASTling)")
    print("=" * 60)
    long_df = pd.read_csv("data/processed/cognates_4lang_long.csv")
    print(f"Shape: {long_df.shape}")
    print(f"\nFirst 10 rows:")
    print(long_df.head(10))
    print(f"\nLanguage counts: {long_df['Language'].value_counts()}")
    
    print("\n" + "=" * 60)
    print("WIDE FORMAT (cognates_4lang_wide.csv - CORRECT)")
    print("=" * 60)
    wide_df = pd.read_csv("data/processed/cognates_4lang_wide.csv", index_col=0)
    print(f"Shape: {wide_df.shape}")
    print(f"Languages (rows): {wide_df.index.tolist()}")
    print(f"Features (cols): {len(wide_df.columns)}")
    print(f"\nFirst 5 features for each language:")
    print(wide_df.iloc[:, :5])
    
    return long_df, wide_df

def create_beastling_format(wide_df):
    """
    BEASTling expects CSV with:
    - First column: language names
    - Remaining columns: binary features (0/1)
    - One row per language
    """
    
    # Reset index to make Language a column
    beastling_df = wide_df.reset_index()
    beastling_df.rename(columns={'index': 'Language'}, inplace=True)
    
    # Save in format BEASTling expects
    output_path = Path("data/processed/dravidian_beastling.csv")
    beastling_df.to_csv(output_path, index=False)
    
    print("\n" + "=" * 60)
    print("CREATED BEASTLING FORMAT")
    print("=" * 60)
    print(f"Saved: {output_path}")
    print(f"Shape: {beastling_df.shape}")
    print(f"Columns: Language + {len(beastling_df.columns)-1} features")
    print(f"\nFirst few columns:")
    print(beastling_df.iloc[:, :6])
    
    return beastling_df

def verify_no_duplicates(df):
    """Verify each language appears exactly once."""
    
    lang_counts = df['Language'].value_counts()
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    print("Language counts (should all be 1):")
    print(lang_counts)
    
    if (lang_counts == 1).all():
        print("✓ No duplicates - ready for BEASTling!")
    else:
        print("✗ Still have duplicates!")
    
    return (lang_counts == 1).all()

if __name__ == "__main__":
    # Check current formats
    long_df, wide_df = check_current_formats()
    
    # Create BEASTling format
    beastling_df = create_beastling_format(wide_df)
    
    # Verify
    verify_no_duplicates(beastling_df)
