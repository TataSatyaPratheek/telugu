# scripts/generate_timeline_svg.py
"""
Generate comprehensive SVG timeline of Dravidian language evolution.
Reverse chronological: Present → Proto-Dravidian (4.22 kya)
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def create_dravidian_timeline_svg():
    """Create detailed SVG timeline combining phylogenetic and historical evidence."""
    
    # SVG dimensions
    width = 1400
    height = 2800
    
    # Create root SVG element
    svg = ET.Element('svg', {
        'width': str(width),
        'height': str(height),
        'xmlns': 'http://www.w3.org/2000/svg',
        'viewBox': f'0 0 {width} {height}'
    })
    
    # Add styles
    style = ET.SubElement(svg, 'style')
    style.text = """
        .title { font: bold 32px sans-serif; fill: #2c3e50; }
        .subtitle { font: 20px sans-serif; fill: #34495e; }
        .period-label { font: bold 18px sans-serif; fill: #2980b9; }
        .date-label { font: 16px monospace; fill: #7f8c8d; }
        .event-title { font: bold 16px sans-serif; fill: #2c3e50; }
        .event-desc { font: 14px sans-serif; fill: #34495e; }
        .category { font: italic 13px sans-serif; fill: #16a085; }
        .phylo-box { fill: #e8f5e9; stroke: #4caf50; stroke-width: 2; }
        .history-box { fill: #fff3e0; stroke: #ff9800; stroke-width: 2; }
        .proto-box { fill: #e3f2fd; stroke: #2196f3; stroke-width: 3; }
        .timeline-line { stroke: #bdc3c7; stroke-width: 3; }
        .branch-line { stroke: #95a5a6; stroke-width: 2; stroke-dasharray: 5,5; }
        .language-node { fill: #3498db; }
    """
    
    # Title
    title = ET.SubElement(svg, 'text', {
        'x': str(width//2), 'y': '40', 
        'class': 'title', 
        'text-anchor': 'middle'
    })
    title.text = 'Dravidian Language Evolution Timeline'
    
    subtitle = ET.SubElement(svg, 'text', {
        'x': str(width//2), 'y': '70',
        'class': 'subtitle',
        'text-anchor': 'middle'
    })
    subtitle.text = 'Telugu, Tamil, Kannada, Malayalam → Proto-Dravidian (Reverse Chronological)'
    
    # Timeline data (reverse chronological: present → past)
    events = [
        # Modern period
        {
            'year': 2025,
            'bce': False,
            'kya': 0,
            'title': 'Present Day',
            'category': 'Modern',
            'languages': ['Telugu', 'Tamil', 'Kannada', 'Malayalam'],
            'desc': 'Four major South Dravidian languages spoken by ~300M people',
            'color': '#27ae60',
            'type': 'modern'
        },
        {
            'year': 2008,
            'bce': False,
            'kya': 0.017,
            'title': 'Telugu Classical Language Status',
            'category': 'Policy',
            'desc': 'Government of India recognizes Telugu as Classical Language',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 1970,
            'bce': False,
            'kya': 0.055,
            'title': 'Modern Linguistic Documentation',
            'category': 'Linguistics',
            'desc': 'Bhadriraju Krishnamurti\'s comparative Dravidian linguistics',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 1525,
            'bce': False,
            'kya': 0.5,
            'title': 'Vijayanagara Classical Period',
            'category': 'Literature',
            'desc': 'Telugu reaches classical zenith; Ashtadiggajas court poets',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 1058,
            'bce': False,
            'kya': 0.967,
            'title': 'Nannaya\'s Andhra Mahabharatam',
            'category': 'Literature',
            'desc': 'Adi Kavi Nannaya inaugurates classical Telugu literature',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 900,
            'bce': False,
            'kya': 1.125,
            'title': 'Malayalam Emergence',
            'category': 'Linguistics',
            'desc': 'Malayalam diverges from Tamil (phylogenetic calibration: 1.2 kya)',
            'color': '#9b59b6',
            'type': 'phylo'
        },
        {
            'year': 660,
            'bce': False,
            'kya': 1.365,
            'title': 'Telugu-Kannada Unified Script',
            'category': 'Script',
            'desc': 'Shared akshara system serves both languages',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 575,
            'bce': False,
            'kya': 1.45,
            'title': 'First Complete Telugu Inscription',
            'category': 'Epigraphy',
            'desc': 'Renati Chola records; Telugu attestation date',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 475,
            'bce': False,
            'kya': 1.55,
            'title': 'Halmidi Inscription (Kannada)',
            'category': 'Epigraphy',
            'desc': 'Earliest Kannada-language epigraph; Kadamba script',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 450,
            'bce': True,
            'kya': 2.475,
            'title': 'Kannada Divergence (Linguistic)',
            'category': 'Linguistics',
            'desc': 'Spoken Kannada emerges (phylogenetic calibration: 2.75 kya)',
            'color': '#9b59b6',
            'type': 'phylo'
        },
        {
            'year': 300,
            'bce': True,
            'kya': 2.325,
            'title': 'Tamil Attestation',
            'category': 'Epigraphy',
            'desc': 'Tamil-Brahmi inscriptions; earliest Tamil writing',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 400,
            'bce': True,
            'kya': 2.425,
            'title': 'Earliest Telugu Lexemes',
            'category': 'Epigraphy',
            'desc': 'Bhattiprolu inscriptions contain Telugu words in Prakrit',
            'color': '#e67e22',
            'type': 'history'
        },
        {
            'year': 1100,
            'bce': True,
            'kya': 3.125,
            'title': 'South Dravidian I-II Split',
            'category': 'Linguistics',
            'desc': 'Telugu lineage separates from Tamil-Kannada-Malayalam branch',
            'color': '#9b59b6',
            'type': 'phylo'
        },
        {
            'year': 1250,
            'bce': True,
            'kya': 3.275,
            'title': 'Telugu Divergence from Proto-Dravidian',
            'category': 'Linguistics',
            'desc': 'Telugu splits as South-Central Dravidian (phylo calibration: 3.25 kya)',
            'color': '#9b59b6',
            'type': 'phylo'
        },
        {
            'year': 1500,
            'bce': True,
            'kya': 3.525,
            'title': 'Tamil Linguistic Emergence',
            'category': 'Linguistics',
            'desc': 'Spoken Tamil develops (phylogenetic calibration: 3.5 kya)',
            'color': '#9b59b6',
            'type': 'phylo'
        },
        {
            'year': 2220,
            'bce': True,
            'kya': 4.22,
            'title': 'PROTO-DRAVIDIAN',
            'category': 'Phylogenetics',
            'desc': 'Common ancestor of all Dravidian languages (Bayesian estimate: 4.22 kya [3.08-5.79])',
            'color': '#2980b9',
            'type': 'proto',
            'phylo_data': {
                'mean': 4.22,
                'hpd_lower': 3.08,
                'hpd_upper': 5.79,
                'kolipakam': 4.65
            }
        },
        {
            'year': 2500,
            'bce': True,
            'kya': 4.5,
            'title': 'Proto-Dravidian Homeland',
            'category': 'Archaeology',
            'desc': 'Southern Neolithic; agriculture, metallurgy, peninsular ecology',
            'color': '#e67e22',
            'type': 'history'
        },
    ]
    
    # Calculate positions
    timeline_x = 200
    timeline_start_y = 120
    event_spacing = 140
    
    # Draw main timeline line
    timeline_height = len(events) * event_spacing
    line = ET.SubElement(svg, 'line', {
        'x1': str(timeline_x),
        'y1': str(timeline_start_y),
        'x2': str(timeline_x),
        'y2': str(timeline_start_y + timeline_height),
        'class': 'timeline-line'
    })
    
    # Draw events
    for i, event in enumerate(events):
        y_pos = timeline_start_y + (i * event_spacing)
        
        # Node on timeline
        node_color = {
            'modern': '#27ae60',
            'history': '#e67e22',
            'phylo': '#9b59b6',
            'proto': '#2196f3'
        }.get(event['type'], '#95a5a6')
        
        node_size = 12 if event['type'] != 'proto' else 18
        circle = ET.SubElement(svg, 'circle', {
            'cx': str(timeline_x),
            'cy': str(y_pos),
            'r': str(node_size),
            'fill': node_color,
            'stroke': '#2c3e50',
            'stroke-width': '2'
        })
        
        # Event box
        box_x = timeline_x + 40
        box_width = width - box_x - 40
        box_height = 110 if event['type'] != 'proto' else 150
        
        box_class = {
            'proto': 'proto-box',
            'phylo': 'phylo-box',
            'history': 'history-box'
        }.get(event['type'], 'history-box')
        
        rect = ET.SubElement(svg, 'rect', {
            'x': str(box_x),
            'y': str(y_pos - box_height//2),
            'width': str(box_width),
            'height': str(box_height),
            'class': box_class,
            'rx': '8'
        })
        
        # Date label
        if event['bce']:
            date_str = f"{event['year']} BCE"
        else:
            date_str = f"{event['year']} CE"
        date_str += f" ({event['kya']:.2f} kya)"
        
        date_text = ET.SubElement(svg, 'text', {
            'x': str(box_x + 10),
            'y': str(y_pos - box_height//2 + 25),
            'class': 'date-label'
        })
        date_text.text = date_str
        
        # Title
        title_text = ET.SubElement(svg, 'text', {
            'x': str(box_x + 10),
            'y': str(y_pos - box_height//2 + 50),
            'class': 'event-title'
        })
        title_text.text = event['title']
        
        # Category
        cat_text = ET.SubElement(svg, 'text', {
            'x': str(box_x + 10),
            'y': str(y_pos - box_height//2 + 70),
            'class': 'category'
        })
        cat_text.text = f"[{event['category']}]"
        
        # Description
        desc_text = ET.SubElement(svg, 'text', {
            'x': str(box_x + 10),
            'y': str(y_pos - box_height//2 + 90),
            'class': 'event-desc'
        })
        desc_text.text = event['desc'][:90] + ('...' if len(event['desc']) > 90 else '')
        
        # Add phylogenetic data for Proto-Dravidian
        if event['type'] == 'proto' and 'phylo_data' in event:
            pd = event['phylo_data']
            phylo_text = ET.SubElement(svg, 'text', {
                'x': str(box_x + 10),
                'y': str(y_pos - box_height//2 + 115),
                'class': 'event-desc',
                'font-weight': 'bold'
            })
            phylo_text.text = f"Bayesian estimate: {pd['mean']:.2f} kya [95% HPD: {pd['hpd_lower']:.2f}-{pd['hpd_upper']:.2f}]"
            
            comp_text = ET.SubElement(svg, 'text', {
                'x': str(box_x + 10),
                'y': str(y_pos - box_height//2 + 135),
                'class': 'event-desc'
            })
            comp_text.text = f"Kolipakam et al. (2018): {pd['kolipakam']} kya [3.0-6.5]; Your 4-lang: {pd['mean']:.2f} kya"
        
        # Languages for modern period
        if 'languages' in event:
            lang_y = y_pos - box_height//2 + 110
            for j, lang in enumerate(event['languages']):
                lang_text = ET.SubElement(svg, 'text', {
                    'x': str(box_x + 10 + (j * 100)),
                    'y': str(lang_y),
                    'font': 'bold 14px sans-serif',
                    'fill': '#2980b9'
                })
                lang_text.text = lang
    
    # Add legend
    legend_y = timeline_start_y + timeline_height + 50
    legend_x = 100
    
    legend_title = ET.SubElement(svg, 'text', {
        'x': str(legend_x),
        'y': str(legend_y),
        'class': 'subtitle'
    })
    legend_title.text = 'Legend:'
    
    legend_items = [
        ('Phylogenetic estimates (Bayesian MCMC)', '#9b59b6'),
        ('Historical/epigraphic evidence', '#e67e22'),
        ('Proto-Dravidian (phylogenetic root)', '#2196f3'),
        ('Modern period', '#27ae60')
    ]
    
    for i, (label, color) in enumerate(legend_items):
        y = legend_y + 30 + (i * 30)
        
        circle = ET.SubElement(svg, 'circle', {
            'cx': str(legend_x + 10),
            'cy': str(y - 5),
            'r': '8',
            'fill': color
        })
        
        text = ET.SubElement(svg, 'text', {
            'x': str(legend_x + 30),
            'y': str(y),
            'font': '14px sans-serif',
            'fill': '#2c3e50'
        })
        text.text = label
    
    # Add methodology note
    method_y = legend_y + 180
    method_text = ET.SubElement(svg, 'text', {
        'x': str(legend_x),
        'y': str(method_y),
        'font': 'italic 12px sans-serif',
        'fill': '#7f8c8d'
    })
    method_text.text = 'Phylogenetic analysis: 267 binary cognate features, 4 languages, Bayesian MCMC (10M samples)'
    
    method_text2 = ET.SubElement(svg, 'text', {
        'x': str(legend_x),
        'y': str(method_y + 20),
        'font': 'italic 12px sans-serif',
        'fill': '#7f8c8d'
    })
    method_text2.text = 'Calibrations: Telugu 3.25 kya, Tamil 3.5 kya, Kannada 2.75 kya, Malayalam 1.2 kya (linguistic divergence dates)'
    
    # Write to file
    tree = ET.ElementTree(svg)
    ET.indent(tree, space="  ")
    
    output_file = Path("results/figures/dravidian_timeline.svg")
    tree.write(output_file, encoding='utf-8', xml_declaration=True)
    
    print(f"✓ Generated: {output_file}")
    print(f"\nTimeline spans: Present (2025 CE) → Proto-Dravidian (~2220 BCE / 4.22 kya)")
    print(f"Total events: {len(events)}")
    print(f"Phylogenetic estimate: 4.22 kya [3.08-5.79 kya 95% HPD]")

if __name__ == "__main__":
    create_dravidian_timeline_svg()
    print("\nTo view: Open results/figures/dravidian_timeline.svg in any web browser")
