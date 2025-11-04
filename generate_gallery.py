#!/usr/bin/env python3
"""
Gallery Generator for Jupyter Notebooks
Scans the notebooks directory and generates an HTML gallery page.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


class NotebookInfo:
    """Information about a notebook for gallery display."""
    
    def __init__(self, path: Path, notebooks_dir: Path):
        self.path = path
        self.relative_path = path.relative_to(notebooks_dir.parent)
        self.name = path.stem
        self.category = path.parent.name
        self.title = self._extract_title()
        self.description = self._extract_description()
        
    def _extract_title(self) -> str:
        """Extract title from notebook, falling back to filename."""
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
                cells = nb_data.get('cells', [])
                
                # Look for first markdown cell with heading
                for cell in cells:
                    if cell.get('cell_type') == 'markdown':
                        source = ''.join(cell.get('source', []))
                        lines = source.strip().split('\n')
                        for line in lines:
                            if line.startswith('#'):
                                # Remove markdown heading syntax
                                return line.lstrip('#').strip()
                
        except (json.JSONDecodeError, IOError):
            pass
        
        # Fallback to filename
        return self.name.replace('_', ' ').replace('-', ' ').title()
    
    def _extract_description(self) -> Optional[str]:
        """Extract description from first markdown cell."""
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
                cells = nb_data.get('cells', [])
                
                # Look for first markdown cell
                for cell in cells:
                    if cell.get('cell_type') == 'markdown':
                        source = ''.join(cell.get('source', []))
                        lines = [l.strip() for l in source.strip().split('\n') if l.strip()]
                        
                        # Skip heading lines, get the first paragraph
                        for line in lines:
                            if not line.startswith('#'):
                                # Limit to 150 characters
                                if len(line) > 150:
                                    return line[:147] + '...'
                                return line
        except (json.JSONDecodeError, IOError):
            pass
        
        return None


def find_notebooks(notebooks_dir: Path) -> List[NotebookInfo]:
    """Find all Jupyter notebooks in the notebooks directory."""
    notebooks = []
    
    for nb_path in notebooks_dir.rglob('*.ipynb'):
        # Skip hidden directories and checkpoint files
        if any(part.startswith('.') for part in nb_path.parts):
            continue
        if '.ipynb_checkpoints' in str(nb_path):
            continue
            
        notebooks.append(NotebookInfo(nb_path, notebooks_dir))
    
    # Sort by category, then by name
    notebooks.sort(key=lambda nb: (nb.category, nb.name))
    return notebooks


def generate_html(notebooks: List[NotebookInfo], output_path: Path):
    """Generate the HTML gallery page."""
    
    # Group notebooks by category
    categories: Dict[str, List[NotebookInfo]] = {}
    for nb in notebooks:
        if nb.category not in categories:
            categories[nb.category] = []
        categories[nb.category].append(nb)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jupyter Notebook Gallery</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem 1rem;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            color: white;
            margin-bottom: 3rem;
        }}
        
        h1 {{
            font-size: 3rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }}
        
        .subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}
        
        .category {{
            margin-bottom: 3rem;
        }}
        
        .category-header {{
            background: rgba(255, 255, 255, 0.95);
            padding: 1rem 1.5rem;
            border-radius: 12px 12px 0 0;
            margin-bottom: 0;
        }}
        
        .category-title {{
            font-size: 1.5rem;
            color: #667eea;
            font-weight: 600;
            text-transform: capitalize;
        }}
        
        .notebook-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            background: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            border-radius: 0 0 12px 12px;
        }}
        
        .notebook-card {{
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            text-decoration: none;
            color: inherit;
            display: block;
            border: 2px solid transparent;
        }}
        
        .notebook-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
            border-color: #667eea;
        }}
        
        .notebook-title {{
            font-size: 1.25rem;
            font-weight: 600;
            color: #667eea;
            margin-bottom: 0.5rem;
        }}
        
        .notebook-description {{
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 1rem;
            line-height: 1.5;
        }}
        
        .notebook-path {{
            font-size: 0.8rem;
            color: #999;
            font-family: 'Courier New', monospace;
        }}
        
        .icon {{
            display: inline-block;
            margin-right: 0.5rem;
            font-size: 1.2rem;
        }}
        
        footer {{
            text-align: center;
            color: white;
            margin-top: 3rem;
            opacity: 0.8;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            h1 {{
                font-size: 2rem;
            }}
            
            .notebook-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📓 Notebook Gallery</h1>
            <p class="subtitle">Browse {len(notebooks)} Jupyter notebooks across {len(categories)} categories</p>
        </header>
        
        <main>
"""
    
    # Generate HTML for each category
    for category_name in sorted(categories.keys()):
        category_notebooks = categories[category_name]
        html += f"""
            <section class="category">
                <div class="category-header">
                    <h2 class="category-title">{category_name}</h2>
                </div>
                <div class="notebook-grid">
"""
        
        for nb in category_notebooks:
            description_html = f'<p class="notebook-description">{nb.description}</p>' if nb.description else ''
            
            html += f"""
                    <a href="{nb.relative_path}" class="notebook-card">
                        <h3 class="notebook-title">
                            <span class="icon">📔</span>{nb.title}
                        </h3>
                        {description_html}
                        <div class="notebook-path">{nb.relative_path}</div>
                    </a>
"""
        
        html += """
                </div>
            </section>
"""
    
    html += f"""
        </main>
        
        <footer>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </footer>
    </div>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    notebooks_dir = script_dir / 'notebooks'
    output_path = script_dir / 'gallery.html'
    
    if not notebooks_dir.exists():
        print(f"Error: Notebooks directory not found: {notebooks_dir}")
        return 1
    
    print(f"Scanning for notebooks in: {notebooks_dir}")
    notebooks = find_notebooks(notebooks_dir)
    print(f"Found {len(notebooks)} notebooks")
    
    print(f"Generating gallery HTML: {output_path}")
    generate_html(notebooks, output_path)
    print(f"Gallery generated successfully!")
    
    return 0


if __name__ == '__main__':
    exit(main())
