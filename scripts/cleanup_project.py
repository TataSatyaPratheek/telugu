# scripts/cleanup_project.py
"""Clean up and organize the Dravidian phylogenetic analysis project."""

import shutil
from pathlib import Path

def cleanup_project():
    """Organize project files, archive unnecessary ones."""
    
    print("="*70)
    print("CLEANING UP DRAVIDIAN PHYLOGENETIC ANALYSIS PROJECT")
    print("="*70)
    
    # Create archive structure
    archive = Path("archive")
    archive.mkdir(exist_ok=True)
    
    archives = {
        'test_runs': archive / "test_runs",
        'beastling_xmls': archive / "beastling_xmls", 
        'unused_scripts': archive / "unused_scripts",
        'old_configs': archive / "old_configs"
    }
    
    for folder in archives.values():
        folder.mkdir(exist_ok=True)
    
    # 1. Move test run files
    print("\n1. Archiving test runs...")
    test_files = [
        "dravidian_beauti_test.log",
        "dravidian_beauti_test-dravidian_4lang.trees",
        "dravidian_beauti_test.xml.state",
        "results/figures/test_run_analysis.png"
    ]
    for f in test_files:
        fp = Path(f)
        if fp.exists():
            shutil.move(str(fp), str(archives['test_runs'] / fp.name))
            print(f"  ✓ Moved {f}")
    
    # 2. Move BEASTling XMLs (we used BEAUti instead)
    print("\n2. Archiving BEASTling XMLs...")
    beastling_xmls = [
        "results/xml/dravidian_4lang_prior.xml",
        "results/xml/dravidian_4lang.xml",
        "results/xml/dravidian_4lang_test.xml",
        "results/xml/dravidian_4lang_test.xml.bak"
    ]
    for f in beastling_xmls:
        fp = Path(f)
        if fp.exists():
            shutil.move(str(fp), str(archives['beastling_xmls'] / fp.name))
            print(f"  ✓ Moved {f}")
    
    # 3. Move unused scripts
    print("\n3. Archiving unused scripts...")
    unused_scripts = [
        "scripts/analyze_test_results.py",
        "scripts/fix_namespace.py",
        "scripts/fix_data_format.py",
        "scripts/create_nexus_final.py",
        "scripts/inspect_data.py",
        "scripts/prepare_data.py"
    ]
    for f in unused_scripts:
        fp = Path(f)
        if fp.exists():
            shutil.move(str(fp), str(archives['unused_scripts'] / fp.name))
            print(f"  ✓ Moved {f}")
    
    # 4. Move old configs
    print("\n4. Archiving old configs...")
    if Path("config/dravidian_test.conf").exists():
        shutil.move("config/dravidian_test.conf", 
                   str(archives['old_configs'] / "dravidian_test.conf"))
        print("  ✓ Moved config/dravidian_test.conf")
    
    # 5. Organize final results
    print("\n5. Organizing final results...")
    final_dir = Path("results/final")
    final_dir.mkdir(exist_ok=True)
    
    final_files = {
        "dravidian_beauti_full.log": "analysis.log",
        "dravidian_beauti_full-dravidian_4lang.trees": "posterior.trees",
        "dravidian_beauti_full.xml.state": "final.xml.state"
    }
    
    for old_name, new_name in final_files.items():
        old_path = Path(old_name)
        if old_path.exists():
            shutil.move(str(old_path), str(final_dir / new_name))
            print(f"  ✓ Moved {old_name} → results/final/{new_name}")
    
    # 6. Clean up empty/redundant files
    print("\n6. Removing redundant files...")
    to_remove = [
        "data/processed/cognates_coded.csv",  # Empty
        "data/processed/cognates_4lang_long.csv"  # Used wide format
    ]
    for f in to_remove:
        fp = Path(f)
        if fp.exists():
            fp.unlink()
            print(f"  ✓ Removed {f}")
    
    # 7. Create README
    print("\n7. Creating README...")
    create_readme()
    
    print("\n" + "="*70)
    print("CLEANUP COMPLETE!")
    print("="*70)
    print("\nFinal structure:")
    print_tree()

def create_readme():
    """Create comprehensive README."""
    
    readme = """# Bayesian Phylogenetic Analysis: Telugu, Tamil, Kannada, Malayalam

## Project Overview

Bayesian phylogenetic analysis of 4 South Dravidian languages using cognate-coded lexical data from the Swadesh 100-word list.

**Analysis Date**: October 29, 2025  
**Method**: Bayesian MCMC using BEAST 2.7.8  
**Data Source**: Kolipakam et al. (2018) supplementary data

## Key Results

### Proto-Dravidian Age Estimate
Run `python scripts/final_analysis.py` to see complete results including:
- Mean age estimate
- 95% HPD interval  
- Comparison with original 20-language study

## Project Structure

```
telugu/
├── config/
│   └── dravidian.conf          # BEASTling configuration (for reference)
├── data/
│   ├── processed/
│   │   ├── dravidian_beastling.csv   # Final binary cognate matrix
│   │   ├── dravidian_4lang.nex       # NEXUS format for BEAUti
│   │   └── dravlex_4lang.csv         # Filtered 4-language data
│   └── raw/
│       └── 2018_02_26_lingpy...      # Original Kolipakam data
├── results/
│   ├── final/
│   │   ├── analysis.log              # BEAST MCMC log (10M samples)
│   │   ├── posterior.trees           # Posterior tree distribution
│   │   └── final.xml.state           # Final MCMC state
│   ├── figures/
│   │   ├── full_analysis.png         # Comprehensive diagnostics
│   │   └── comparison_kolipakam.png  # Comparison with original study
│   └── xml/
│       ├── dravidian_beauti_full.xml # BEAST XML (used for analysis)
│       └── dravidian_beauti_test.xml # Test run XML
├── scripts/
│   ├── extract_4lang.py       # Extract 4 languages from source data
│   ├── analyze_full_results.py # Analyze BEAST results  
│   └── final_analysis.py      # Generate final plots and statistics
├── archive/
│   ├── test_runs/             # Test run files
│   ├── beastling_xmls/        # BEASTling-generated XMLs (not used)
│   └── unused_scripts/        # Scripts used during development
└── README.md

```

## Reproduce the Analysis

### Prerequisites
- Python 3.11+ with uv
- BEAST 2.7+ 
- Java 17+

### Installation
```
# Install dependencies
uv sync

# Add BEAST to PATH
export PATH="/Applications/BEAST 2.7.7/bin:$PATH"
```

### Run Analysis

1. **Data already prepared** in `data/processed/`

2. **To re-run BEAST analysis**:
```
# Open BEAUti and load data/processed/dravidian_4lang.nex
beauti

# Or use existing XML:
beast -threads 3 results/xml/dravidian_beauti_full.xml
```

3. **Analyze results**:
```
uv run python scripts/final_analysis.py
```

## Data Description

### Languages
- **Telugu**: 1.45 kya (earliest attestation ~575 CE)
- **Tamil**: 2.323 kya (earliest attestation ~300 BCE)  
- **Kannada**: 1.575 kya (earliest attestation ~450 CE)
- **Malayalam**: 1.195 kya (earliest attestation ~830 CE)

### Features
- 267 binary cognate features from Swadesh 100-word list
- Cognate assignments from Dravidian Etymological Dictionary (DEDR)

### Model
- **Substitution**: Mutation Death Model (binary data)
- **Clock**: Relaxed Clock Log Normal
- **Tree Prior**: Yule Model (pure birth)
- **MCMC**: 10 million samples, 10% burnin

## Citations

**Original data source:**
Kolipakam, V., et al. (2018). A Bayesian phylogenetic study of the Dravidian language family. *Royal Society Open Science*, 5(3), 171504.

**Software:**
Bouckaert, R., et al. (2019). BEAST 2.5: An advanced software platform for Bayesian evolutionary analysis. *PLoS Computational Biology*, 15(4), e1006650.

## License

Analysis code: MIT License  
Data: See Kolipakam et al. (2018) supplementary materials

## Contact

Generated as part of Telugu linguistic research project.
"""
    
    Path("README.md").write_text(readme)
    print("  ✓ Created README.md")

def print_tree():
    """Print simplified tree structure."""
    print("""
    telugu/
    ├── config/              # Configuration files
    ├── data/
    │   ├── processed/       # Final data files
    │   └── raw/            # Original source data
    ├── results/
    │   ├── final/          # Main results (10M MCMC run)
    │   ├── figures/        # Publication plots
    │   └── xml/            # BEAST XML files
    ├── scripts/            # Analysis scripts (3 core files)
    ├── archive/            # Old/test files
    └── README.md
    """)

if __name__ == "__main__":
    cleanup_project()
