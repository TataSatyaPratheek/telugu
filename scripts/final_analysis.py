# scripts/final_analysis.py
"""Complete analysis of Dravidian phylogenetic results."""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300

def analyze_full_results():
    """Comprehensive analysis of 10M MCMC run."""
    
    # Load log
    print("Loading full analysis results...")
    df = pd.read_csv("dravidian_beauti_full.log", sep="\t", comment="#")
    
    # Remove 10% burnin
    burnin_samples = int(len(df) * 0.1)
    df_post = df.iloc[burnin_samples:]
    
    print(f"\n{'='*70}")
    print("PROTO-DRAVIDIAN AGE ESTIMATE")
    print(f"{'='*70}")
    
    # Tree Height = Proto-Dravidian age
    tree_height = df_post['Tree.height']
    
    mean_age = tree_height.mean()
    median_age = tree_height.median()
    hpd_lower = tree_height.quantile(0.025)
    hpd_upper = tree_height.quantile(0.975)
    
    print(f"\nYour 4-language analysis:")
    print(f"  Mean:      {mean_age:.2f} kya (thousand years ago)")
    print(f"  Median:    {median_age:.2f} kya")
    print(f"  95% HPD:   [{hpd_lower:.2f}, {hpd_upper:.2f}] kya")
    
    print(f"\nOriginal Kolipakam et al. (2018) - 20 languages:")
    print(f"  Mean:      4.65 kya")
    print(f"  95% HPD:   [3.0, 6.5] kya")
    
    print(f"\n{'='*70}")
    print("LANGUAGE DIVERGENCE ESTIMATES")
    print(f"{'='*70}")
    
    # Calculate approx divergence times based on tree height
    print(f"\nEstimated divergence ages (from present):")
    print(f"  Proto-Dravidian:     ~{mean_age:.0f} kya")
    print(f"  Tamil (attested):    2.323 kya (300 BCE)")
    print(f"  Telugu (attested):   1.45 kya (575 CE)")
    print(f"  Kannada (attested):  1.575 kya (450 CE)")
    print(f"  Malayalam (attested): 1.195 kya (830 CE)")
    
    # Convergence diagnostics
    print(f"\n{'='*70}")
    print("CONVERGENCE DIAGNOSTICS")
    print(f"{'='*70}")
    
    print(f"\nPosterior:")
    print(f"  Starting: {df['posterior'].iloc[0]:.2f}")
    print(f"  Final:    {df['posterior'].iloc[-1]:.2f}")
    print(f"  Mean:     {df_post['posterior'].mean():.2f}")
    
    print(f"\nLikelihood:")
    print(f"  Mean: {df_post['likelihood'].mean():.2f}")
    
    # Create comprehensive plots
    create_publication_plots(df, df_post, mean_age, hpd_lower, hpd_upper)
    
    # Save summary
    summary = {
        'mean_age': mean_age,
        'median_age': median_age,
        'hpd_lower': hpd_lower,
        'hpd_upper': hpd_upper,
        'total_samples': len(df),
        'post_burnin_samples': len(df_post)
    }
    
    return df_post, summary

def create_publication_plots(df, df_post, mean_age, hpd_lower, hpd_upper):
    """Create publication-quality plots."""
    
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 1. Posterior trace
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(df['posterior'], alpha=0.5, linewidth=0.3, color='steelblue')
    ax1.axvline(len(df)*0.1, color='red', linestyle='--', label='Burnin (10%)', linewidth=2)
    ax1.set_xlabel('MCMC Sample')
    ax1.set_ylabel('Log Posterior')
    ax1.set_title('A. MCMC Trace: Posterior', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(alpha=0.3)
    
    # 2. Likelihood trace
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.plot(df['likelihood'], alpha=0.5, linewidth=0.3, color='darkgreen')
    ax2.axvline(len(df)*0.1, color='red', linestyle='--', linewidth=2)
    ax2.set_xlabel('MCMC Sample')
    ax2.set_ylabel('Log Likelihood')
    ax2.set_title('B. Likelihood Trace', fontsize=12, fontweight='bold')
    ax2.grid(alpha=0.3)
    
    # 3. Tree Height trace (Proto-Dravidian age)
    ax3 = fig.add_subplot(gs[1, :2])
    ax3.plot(df['Tree.height'], alpha=0.5, linewidth=0.3, color='darkred')
    ax3.axvline(len(df)*0.1, color='red', linestyle='--', linewidth=2)
    ax3.axhline(4.65, color='blue', linestyle=':', label='Kolipakam et al. (2018): 4.65 kya', linewidth=2)
    ax3.set_xlabel('MCMC Sample')
    ax3.set_ylabel('Age (kya)')
    ax3.set_title('C. MCMC Trace: Proto-Dravidian Age', fontsize=12, fontweight='bold')
    ax3.legend()
    ax3.grid(alpha=0.3)
    
    # 4. Proto-Dravidian Age Distribution
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.hist(df_post['Tree.height'], bins=50, alpha=0.7, color='coral', edgecolor='black')
    ax4.axvline(mean_age, color='darkred', linestyle='-', linewidth=2, label=f'Mean: {mean_age:.2f} kya')
    ax4.axvline(hpd_lower, color='gray', linestyle='--', linewidth=1.5, label=f'95% HPD')
    ax4.axvline(hpd_upper, color='gray', linestyle='--', linewidth=1.5)
    ax4.axvline(4.65, color='blue', linestyle=':', linewidth=2, label='Kolipakam: 4.65 kya')
    ax4.set_xlabel('Age (kya)')
    ax4.set_ylabel('Frequency')
    ax4.set_title('D. Proto-Dravidian Age', fontsize=12, fontweight='bold')
    ax4.legend(fontsize=8)
    ax4.grid(alpha=0.3)
    
    # 5. Clock Rate trace
    ax5 = fig.add_subplot(gs[2, 0])
    ax5.plot(df['ucldMean'], alpha=0.5, linewidth=0.3, color='purple')
    ax5.axvline(len(df)*0.1, color='red', linestyle='--', linewidth=2)
    ax5.set_xlabel('MCMC Sample')
    ax5.set_ylabel('Clock Rate')
    ax5.set_title('E. Relaxed Clock Mean', fontsize=12, fontweight='bold')
    ax5.grid(alpha=0.3)
    
    # 6. Birth Rate
    ax6 = fig.add_subplot(gs[2, 1])
    ax6.plot(df['birthRate'], alpha=0.5, linewidth=0.3, color='green')
    ax6.axvline(len(df)*0.1, color='red', linestyle='--', linewidth=2)
    ax6.set_xlabel('MCMC Sample')
    ax6.set_ylabel('Birth Rate')
    ax6.set_title('F. Yule Birth Rate', fontsize=12, fontweight='bold')
    ax6.grid(alpha=0.3)
    
    # 7. Tree Length
    ax7 = fig.add_subplot(gs[2, 2])
    ax7.plot(df['Tree.treeLength'], alpha=0.5, linewidth=0.3, color='brown')
    ax7.axvline(len(df)*0.1, color='red', linestyle='--', linewidth=2)
    ax7.set_xlabel('MCMC Sample')
    ax7.set_ylabel('Tree Length')
    ax7.set_title('G. Total Tree Length', fontsize=12, fontweight='bold')
    ax7.grid(alpha=0.3)
    
    fig.suptitle('Bayesian Phylogenetic Analysis: Telugu, Tamil, Kannada, Malayalam', 
                 fontsize=14, fontweight='bold', y=0.995)
    
    plt.savefig('results/figures/full_analysis.png', dpi=300, bbox_inches='tight')
    print(f"\n✓ Saved: results/figures/full_analysis.png")
    
    # Create simplified comparison plot
    create_comparison_plot(df_post, mean_age, hpd_lower, hpd_upper)

def create_comparison_plot(df_post, mean_age, hpd_lower, hpd_upper):
    """Create comparison with original study."""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Your results
    ax.hist(df_post['Tree.height'], bins=50, alpha=0.6, color='coral', 
            label='This study (4 languages)', edgecolor='black')
    ax.axvline(mean_age, color='darkred', linestyle='-', linewidth=2, 
               label=f'Mean: {mean_age:.2f} kya')
    ax.axvspan(hpd_lower, hpd_upper, alpha=0.2, color='red', 
               label=f'95% HPD: [{hpd_lower:.2f}, {hpd_upper:.2f}]')
    
    # Kolipakam comparison
    ax.axvline(4.65, color='blue', linestyle='--', linewidth=2, 
               label='Kolipakam et al. 2018: 4.65 kya')
    ax.axvspan(3.0, 6.5, alpha=0.1, color='blue', 
               label='Kolipakam 95% HPD: [3.0, 6.5]')
    
    ax.set_xlabel('Proto-Dravidian Age (thousand years ago)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Proto-Dravidian Age Estimate:\nComparison with Kolipakam et al. (2018)', 
                 fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('results/figures/comparison_kolipakam.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: results/figures/comparison_kolipakam.png")

if __name__ == "__main__":
    results, summary = analyze_full_results()
    
    print(f"\n{'='*70}")
    print("ANALYSIS COMPLETE!")
    print(f"{'='*70}")
    print("\nNext steps:")
    print("1. Visualize tree: treeannotator + FigTree")
    print("2. Check trace files in Tracer")
    print("3. Write up results!")
