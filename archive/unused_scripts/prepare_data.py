"""Prepare Swadesh 100-word list data for phylogenetic analysis."""

import pandas as pd
from pathlib import Path

# Define basic structure
DATA_RAW = Path("data/raw")
DATA_PROCESSED = Path("data/processed")

# Swadesh 100-word list (core stable vocabulary)
SWADESH_100 = [
    "I", "you", "we", "this", "that", "who", "what", "not", "all", "many",
    "one", "two", "big", "long", "small", "woman", "man", "person", "fish",
    "bird", "dog", "louse", "tree", "seed", "leaf", "root", "bark", "skin",
    "flesh", "blood", "bone", "grease", "egg", "horn", "tail", "feather",
    "hair", "head", "ear", "eye", "nose", "mouth", "tooth", "tongue", "claw",
    "foot", "knee", "hand", "belly", "neck", "breasts", "heart", "liver",
    "drink", "eat", "bite", "see", "hear", "know", "sleep", "die", "kill",
    "swim", "fly", "walk", "come", "lie", "sit", "stand", "give", "say",
    "sun", "moon", "star", "water", "rain", "stone", "sand", "earth", "cloud",
    "smoke", "fire", "ash", "burn", "path", "mountain", "red", "green",
    "yellow", "white", "black", "night", "hot", "cold", "full", "new",
    "good", "round", "dry", "name"
]

def create_template():
    """Create empty template for data collection."""
    languages = ["Telugu", "Tamil", "Kannada", "Malayalam"]
    
    df = pd.DataFrame({
        "Language_ID": [lang for lang in languages for _ in SWADESH_100],
        "Feature_ID": SWADESH_100 * len(languages),
        "IPA": ["" for _ in range(len(languages) * len(SWADESH_100))],
        "Cognate_Class": ["" for _ in range(len(languages) * len(SWADESH_100))],
    })
    
    output_path = DATA_RAW / "swadesh_4lang_template.csv"
    df.to_csv(output_path, index=False)
    print(f"Template created: {output_path}")
    print(f"\nInstructions:")
    print("1. Fill IPA column with phonetic transcriptions")
    print("2. Fill Cognate_Class with numbers (same number = cognate)")
    print("3. Use DEDR (http://dsal.uchicago.edu/dictionaries/burrow/)")
    print("4. Save as swadesh_4lang.csv")

def code_cognates(input_file: str, output_file: str):
    """Convert cognate classes to binary presence/absence matrix."""
    df = pd.read_csv(DATA_RAW / input_file)
    
    # Get unique cognate classes per meaning
    binary_data = []
    
    for meaning in SWADESH_100:
        meaning_data = df[df["Feature_ID"] == meaning]
        cognate_classes = meaning_data["Cognate_Class"].unique()
        
        # Remove NaN and empty
        cognate_classes = [c for c in cognate_classes if pd.notna(c) and c != ""]
        
        for cognate_class in cognate_classes:
            feature_name = f"{meaning}_{cognate_class}"
            for lang in ["Telugu", "Tamil", "Kannada", "Malayalam"]:
                lang_data = meaning_data[meaning_data["Language_ID"] == lang]
                has_cognate = cognate_class in lang_data["Cognate_Class"].values
                binary_data.append({
                    "Language_ID": lang,
                    "Feature_ID": feature_name,
                    "Value": 1 if has_cognate else 0
                })
    
    binary_df = pd.DataFrame(binary_data)
    output_path = DATA_PROCESSED / output_file
    binary_df.to_csv(output_path, index=False)
    print(f"Binary cognate matrix created: {output_path}")
    return binary_df

if __name__ == "__main__":
    create_template()