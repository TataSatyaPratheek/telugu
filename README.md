# Bayesian Phylogenetic Analysis: Telugu, Tamil, Kannada, Malayalam

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
