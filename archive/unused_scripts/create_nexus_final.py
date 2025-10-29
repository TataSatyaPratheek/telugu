"""Create NEXUS file for BEAUti - the correct way."""

import pandas as pd
from pathlib import Path

def create_nexus_for_beauti():
    """Create properly formatted NEXUS file."""
    
    # Load your binary data
    df = pd.read_csv("data/processed/dravidian_beastling.csv")
    
    # Get languages and data
    languages = df.iloc[:, 0].tolist()
    binary_data = df.iloc[:, 1:].values
    
    n_taxa = len(languages)
    n_chars = binary_data.shape[1]
    
    print(f"Creating NEXUS with {n_taxa} taxa and {n_chars} characters...")
    
    # Create NEXUS format
    nexus = []
    nexus.append("#NEXUS")
    nexus.append("")
    nexus.append("BEGIN DATA;")
    nexus.append(f"    DIMENSIONS NTAX={n_taxa} NCHAR={n_chars};")
    nexus.append("    FORMAT DATATYPE=STANDARD MISSING=? GAP=- SYMBOLS=\"01\";")
    nexus.append("    MATRIX")
    
    for i, lang in enumerate(languages):
        sequence = ''.join(str(int(x)) for x in binary_data[i])
        nexus.append(f"        {lang:<20} {sequence}")
    
    nexus.append("    ;")
    nexus.append("END;")
    
    # Save
    output = Path("data/processed/dravidian_4lang.nex")
    with open(output, 'w') as f:
        f.write('\n'.join(nexus))
    
    print(f"✓ Created: {output}")
    print(f"\nNext steps:")
    print("1. Open BEAUti:  beauti")
    print("2. File > Import Alignment")
    print("3. Select: data/processed/dravidian_4lang.nex")
    print("4. Configure analysis in BEAUti GUI")
    
    return output

if __name__ == "__main__":
    create_nexus_for_beauti()
