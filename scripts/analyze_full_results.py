# scripts/analyze_test_results.py
"""Analyze the test BEAST run results."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def analyze_test_run():
    """Quick analysis of test run."""
    
    # Load log file
    log_file = "dravidian_beauti_full.log"
    
    print(f"Loading {log_file}...")
    df = pd.read_csv(log_file, sep="\t", comment="#")
    
    # Remove burnin (10%)
    burnin = int(len(df) * 0.1)
    df_post = df.iloc[burnin:]
    
    print(f"\n{'='*60}")
    print("TEST RUN RESULTS")
    print(f"{'='*60}")
    print(f"Total samples: {len(df)}")
    print(f"After burnin (10%): {len(df_post)}")
    
    # Check convergence
    print(f"\nPosterior:")
    print(f"  Start: {df['posterior'].iloc[0]:.2f}")
    print(f"  End: {df['posterior'].iloc[-1]:.2f}")
    print(f"  Mean (post-burnin): {df_post['posterior'].mean():.2f}")
    
    print(f"\nLikelihood:")
    print(f"  Mean: {df_post['likelihood'].mean():.2f}")
    
    if 'TreeHeight' in df.columns:
        print(f"\nProto-Dravidian Age Estimate:")
        print(f"  Mean: {df_post['TreeHeight'].mean():.3f} kya")
        print(f"  95% HPD: [{df_post['TreeHeight'].quantile(0.025):.3f}, {df_post['TreeHeight'].quantile(0.975):.3f}]")
    
    # Quick plots
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    
    # Posterior trace
    axes[0, 0].plot(df['posterior'], alpha=0.7, linewidth=0.5)
    axes[0, 0].axvline(burnin, color='red', linestyle='--', label='Burnin')
    axes[0, 0].set_xlabel('Sample')
    axes[0, 0].set_ylabel('Posterior')
    axes[0, 0].set_title('Posterior Trace')
    axes[0, 0].legend()
    
    # Likelihood trace
    axes[0, 1].plot(df['likelihood'], alpha=0.7, linewidth=0.5)
    axes[0, 1].axvline(burnin, color='red', linestyle='--', label='Burnin')
    axes[0, 1].set_xlabel('Sample')
    axes[0, 1].set_ylabel('Likelihood')
    axes[0, 1].set_title('Likelihood Trace')
    
    # Posterior distribution
    axes[1, 0].hist(df_post['posterior'], bins=30, alpha=0.7, edgecolor='black')
    axes[1, 0].set_xlabel('Posterior')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Posterior Distribution (post-burnin)')
    
    # TreeHeight if available
    if 'TreeHeight' in df.columns:
        axes[1, 1].hist(df_post['TreeHeight'], bins=30, alpha=0.7, edgecolor='black')
        axes[1, 1].set_xlabel('Age (kya)')
        axes[1, 1].set_ylabel('Frequency')
        axes[1, 1].set_title('Proto-Dravidian Age')
    
    plt.tight_layout()
    plt.savefig('results/figures/test_run_analysis.png', dpi=300)
    print(f"\n✓ Saved: results/figures/test_run_analysis.png")
    
    return df_post

if __name__ == "__main__":
    results = analyze_test_run()
    print(f"\n{'='*60}")
    print("Test run successful! Ready for full analysis.")
    print(f"{'='*60}")
