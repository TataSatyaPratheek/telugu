# scripts/extract_4lang.py
"""Extract Telugu, Tamil, Kannada, Malayalam and convert to binary format."""

import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw/2018_02_26_lingpy_analyses_for_RSOS_SI_ SI_robustness_cognate_coding")
PROCESSED_DIR = Path("data/processed")

# Target languages - check exact names in languages.csv first
TARGET_LANGS = {
    "Telugu": "Telugu",
    "Tamil": "Tamil", 
    "Kannada": "Kannada",
    "Malayalam": "Malayalam"
}

def extract_cognate_data():
    """Extract 4-language cognate data from DravLex."""
    
    # Load the main data (TSV is the LingPy format)
    print("Loading DravLex.tsv...")
    df = pd.read_csv(RAW_DIR / "DravLex.tsv", sep="\t")
    
    # Check column names (common LingPy columns: ID, DOCULECT, CONCEPT, IPA, TOKENS, COGID)
    print(f"Columns: {df.columns.tolist()}\n")
    
    # Filter for 4 languages
    # Adjust column name if needed (might be 'DOCULECT', 'Language', or 'Language_ID')
    lang_col = 'DOCULECT' if 'DOCULECT' in df.columns else 'Language'
    
    target_lang_values = list(TARGET_LANGS.values())
    df_filtered = df[df[lang_col].isin(target_lang_values)].copy()
    
    print(f"Filtered to {len(df_filtered)} entries")
    print(f"Languages: {df_filtered[lang_col].unique()}")
    print(f"Concepts: {df_filtered['CONCEPT'].nunique() if 'CONCEPT' in df_filtered.columns else 'Check column'}")
    
    # Save intermediate filtered data
    df_filtered.to_csv(PROCESSED_DIR / "dravlex_4lang.csv", index=False)
    print(f"\nSaved: {PROCESSED_DIR / 'dravlex_4lang.csv'}")
    
    return df_filtered

def convert_to_binary(df):
    """
    Convert cognate classes to binary presence/absence matrix.
    
    LingPy format has COGID (cognate ID) for each word.
    Same COGID across languages = cognate.
    """
    
    lang_col = 'DOCULECT' if 'DOCULECT' in df.columns else 'Language'
    concept_col = 'CONCEPT'
    cogid_col = 'COGID'
    
    # Create binary matrix
    binary_data = []
    
    # Group by concept
    for concept, concept_df in df.groupby(concept_col):
        # Get all unique cognate classes for this concept
        cognate_classes = concept_df[cogid_col].unique()
        
        # For each cognate class, create a binary feature
        for cog_id in cognate_classes:
            if pd.isna(cog_id) or cog_id == 0:  # Skip missing data
                continue
                
            feature_name = f"{concept}_{int(cog_id)}"
            
            # Check which languages have this cognate
            for lang in TARGET_LANGS.values():
                lang_data = concept_df[concept_df[lang_col] == lang]
                has_cognate = int(cog_id in lang_data[cogid_col].values)
                
                binary_data.append({
                    'Language': lang,
                    'Feature': feature_name,
                    'Value': has_cognate
                })
    
    binary_df = pd.DataFrame(binary_data)
    
    # Pivot to wide format (languages as rows, features as columns)
    binary_wide = binary_df.pivot(index='Language', columns='Feature', values='Value')
    binary_wide = binary_wide.fillna(0).astype(int)
    
    print(f"\nBinary matrix shape: {binary_wide.shape}")
    print(f"Languages: {len(binary_wide)}")
    print(f"Features (cognate classes): {len(binary_wide.columns)}")
    
    # Save both formats
    binary_df.to_csv(PROCESSED_DIR / "cognates_4lang_long.csv", index=False)
    binary_wide.to_csv(PROCESSED_DIR / "cognates_4lang_wide.csv")
    
    print(f"\nSaved: {PROCESSED_DIR / 'cognates_4lang_long.csv'}")
    print(f"Saved: {PROCESSED_DIR / 'cognates_4lang_wide.csv'}")
    
    return binary_df, binary_wide

if __name__ == "__main__":
    # Extract 4-language data
    df_4lang = extract_cognate_data()
    
    # Convert to binary
    binary_long, binary_wide = convert_to_binary(df_4lang)
    
    print("\n" + "=" * 60)
    print("Data preparation complete!")
    print("=" * 60)
    print("\nNext step: Generate BEAST XML with BEASTling")
