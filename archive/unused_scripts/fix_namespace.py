"""Fix BEAST 2.0 namespace to BEAST 2.7+ namespace."""

from pathlib import Path
import re

def fix_beast_namespace(xml_file):
    """Convert BEAST 2.0 namespace to BEAST 2.7+ namespace."""
    
    xml_path = Path(xml_file)
    print(f"\nFixing {xml_path}...")
    
    with open(xml_path, 'r') as f:
        content = f.read()
    
    # Line 2: Fix namespace declaration
    old_namespace = 'namespace="beast.core:beast.evolution.alignment:beast.evolution.tree.coalescent:beast.core.util:beast.evolution.nuc:beast.evolution.operators:beast.evolution.sitemodel:beast.evolution.substitutionmodel:beast.evolution.likelihood"'
    new_namespace = 'namespace="beast.base.core:beast.base.inference:beast.base.evolution.alignment:beast.base.evolution.tree.coalescent:beast.base.util:beast.base.math:beast.base.evolution.operator:beast.base.inference.operator:beast.base.evolution.sitemodel:beast.base.evolution.substitutionmodel:beast.base.evolution.likelihood"'
    
    content = content.replace(old_namespace, new_namespace)
    
    # Fix all map declarations
    map_fixes = {
        'beast.math.distributions.Beta': 'beast.base.inference.distribution.Beta',
        'beast.math.distributions.Exponential': 'beast.base.inference.distribution.Exponential',
        'beast.math.distributions.InverseGamma': 'beast.base.inference.distribution.InverseGamma',
        'beast.math.distributions.LogNormalDistributionModel': 'beast.base.inference.distribution.LogNormalDistributionModel',
        'beast.math.distributions.Gamma': 'beast.base.inference.distribution.Gamma',
        'beast.math.distributions.Uniform': 'beast.base.inference.distribution.Uniform',
        'beast.math.distributions.LaplaceDistribution': 'beast.base.inference.distribution.LaplaceDistribution',
        'beast.math.distributions.OneOnX': 'beast.base.inference.distribution.OneOnX',
        'beast.math.distributions.Normal': 'beast.base.inference.distribution.Normal',
        'beast.math.distributions.Prior': 'beast.base.inference.distribution.Prior',
        'beast.evolution.alignment.Taxon': 'beast.base.evolution.alignment.Taxon',
        'beast.evolution.alignment.TaxonSet': 'beast.base.evolution.alignment.TaxonSet',
    }
    
    for old, new in map_fixes.items():
        content = content.replace(old, new)
    
    # Fix spec="MCMC" (line 59 uses double quotes)
    content = content.replace('spec="MCMC"', 'spec="beast.base.inference.MCMC"')
    
    # Fix all other beast.core and beast.evolution references
    namespace_replacements = [
        ('beast.core.parameter.', 'beast.base.inference.parameter.'),
        ('beast.core.util.', 'beast.base.util.'),
        ('beast.core.', 'beast.base.inference.'),
        ('beast.evolution.alignment.', 'beast.base.evolution.alignment.'),
        ('beast.evolution.tree.', 'beast.base.evolution.tree.'),
        ('beast.evolution.operators.', 'beast.base.evolution.operators.'),
        ('beast.evolution.sitemodel.', 'beast.base.evolution.sitemodel.'),
        ('beast.evolution.substitutionmodel.', 'beast.base.evolution.substitutionmodel.'),
        ('beast.evolution.likelihood.', 'beast.base.evolution.likelihood.'),
        ('beast.evolution.branchratemodel.', 'beast.base.evolution.branchratemodel.'),
        ('beast.evolution.speciation.', 'beast.base.evolution.speciation.'),
        ('beast.math.', 'beast.base.math.'),
    ]
    
    for old, new in namespace_replacements:
        content = content.replace(old, new)
    
    # Save the fixed version
    with open(xml_path, 'w') as f:
        f.write(content)
    
    print(f"✓ Fixed namespaces in {xml_path}")
    
    # Verify key changes
    if 'beast.base.inference.MCMC' in content:
        print("  ✓ MCMC spec updated")
    if 'namespace="beast.base.' in content:
        print("  ✓ Namespace declaration updated")
    
    return xml_path

if __name__ == "__main__":
    xml_files = [
        "results/xml/dravidian_4lang_test.xml",
        "results/xml/dravidian_4lang_prior.xml",
        "results/xml/dravidian_4lang.xml",
    ]
    
    print("="*60)
    print("Fixing BEAST XML files for version 2.7+ compatibility")
    print("="*60)
    
    for xml_file in xml_files:
        if Path(xml_file).exists():
            fix_beast_namespace(xml_file)
        else:
            print(f"\nSkipping {xml_file} (not found)")
    
    print("\n" + "="*60)
    print("Done! Now try running:")
    print("  beast -threads 3 -beagle_CPU results/xml/dravidian_4lang_test.xml")
    print("="*60)
