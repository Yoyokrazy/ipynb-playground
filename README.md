# Jupyter Notebook Playground

A collection of Jupyter notebooks for various data analysis and programming examples.

## Gallery Generator

This repository includes a gallery generator that creates a beautiful HTML page to browse all notebooks.

### Usage

Generate the gallery by running:

```bash
python3 generate_gallery.py
```

This will:
- Scan all `.ipynb` files in the `notebooks/` directory
- Extract titles and descriptions from the notebooks
- Generate a responsive HTML gallery at `gallery.html`

### Features

- **Automatic Discovery**: Finds all notebooks in subdirectories
- **Smart Titles**: Extracts titles from markdown cells or uses filename
- **Categories**: Organizes notebooks by their folder location
- **Descriptions**: Shows the first paragraph from markdown cells
- **Responsive Design**: Works on desktop and mobile devices
- **Beautiful UI**: Modern gradient design with card-based layout

### Notebooks

Browse the collection at `gallery.html` after generation, or explore the directories:

- `notebooks/cycling/` - Cycling performance analysis
- `notebooks/titanic/` - Machine learning with Titanic dataset
- `notebooks/rich notebooks/` - Feature-rich notebook examples
- `notebooks/simple notebooks/` - Simple demonstration notebooks

## Development

The gallery generator is written in Python 3 and has no external dependencies - it uses only standard library modules.
