#!/bin/bash

# Create output directories

echo "Creating output directories for sensitivity analyses..."
mkdir -p results/sensitivity/{medium,loose,tight}

echo "Running sensitivity analysis: 3 different tree height priors"
echo "============================================================"

# Medium prior (recommended)
echo "1. Running MEDIUM prior (Sigma=1.0)..."
beast -threads 3 -beagle_CPU results/xml/dravidian_medium_prior.xml
mv dravidian_medium*.* results/sensitivity/medium/

# Loose prior
echo "2. Running LOOSE prior (Sigma=1.5)..."
beast -threads 3 -beagle_CPU results/xml/dravidian_loose_prior.xml
mv dravidian_loose*.* results/sensitivity/loose/

# Tight prior
echo "3. Running TIGHT prior (Sigma=0.5)..."
beast -threads 3 -beagle_CPU results/xml/dravidian_tight_prior.xml
mv dravidian_tight*.* results/sensitivity/tight/

echo "All analyses complete!"

