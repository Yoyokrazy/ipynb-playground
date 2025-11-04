"""
Unit tests for the gallery generator
"""
import sys
import os
from pathlib import Path

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from generate_gallery import NotebookInfo, find_notebooks, generate_html


def test_find_notebooks():
    """Test that we can find notebooks in the notebooks directory"""
    notebooks_dir = Path(__file__).parent.parent / 'notebooks'
    
    if not notebooks_dir.exists():
        print("⚠ Notebooks directory not found, skipping test")
        return
    
    notebooks = find_notebooks(notebooks_dir)
    
    # We should find at least some notebooks
    assert len(notebooks) > 0, "Should find at least one notebook"
    
    # Check that all found files are .ipynb files
    for nb in notebooks:
        assert nb.path.suffix == '.ipynb', f"Expected .ipynb file, got {nb.path.suffix}"
        assert nb.path.exists(), f"Notebook path should exist: {nb.path}"
    
    print(f"✓ Found {len(notebooks)} notebooks")


def test_notebook_info():
    """Test NotebookInfo class"""
    notebooks_dir = Path(__file__).parent.parent / 'notebooks'
    
    if not notebooks_dir.exists():
        print("⚠ Notebooks directory not found, skipping test")
        return
    
    notebooks = find_notebooks(notebooks_dir)
    
    if len(notebooks) == 0:
        print("⚠ No notebooks found, skipping test")
        return
    
    # Test the first notebook
    nb = notebooks[0]
    
    # Should have all required attributes
    assert hasattr(nb, 'path'), "Should have path"
    assert hasattr(nb, 'title'), "Should have title"
    assert hasattr(nb, 'category'), "Should have category"
    assert hasattr(nb, 'relative_path'), "Should have relative_path"
    
    # Title should not be empty
    assert len(nb.title) > 0, "Title should not be empty"
    
    # Category should not be empty
    assert len(nb.category) > 0, "Category should not be empty"
    
    print(f"✓ NotebookInfo test passed for: {nb.title}")


def test_generate_html():
    """Test HTML generation"""
    import tempfile
    
    notebooks_dir = Path(__file__).parent.parent / 'notebooks'
    
    if not notebooks_dir.exists():
        print("⚠ Notebooks directory not found, skipping test")
        return
    
    notebooks = find_notebooks(notebooks_dir)
    
    if len(notebooks) == 0:
        print("⚠ No notebooks found, skipping test")
        return
    
    # Generate HTML to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
        temp_path = Path(f.name)
    
    try:
        generate_html(notebooks, temp_path)
        
        # Check that file was created
        assert temp_path.exists(), "HTML file should be created"
        
        # Check that file has content
        content = temp_path.read_text(encoding='utf-8')
        assert len(content) > 0, "HTML should have content"
        
        # Check for expected HTML elements
        assert '<!DOCTYPE html>' in content, "Should have DOCTYPE"
        assert '<html' in content, "Should have html tag"
        assert 'Notebook Gallery' in content, "Should have gallery title"
        assert f'{len(notebooks)}' in content, "Should mention number of notebooks"
        
        print(f"✓ Generated HTML with {len(content)} characters")
    
    finally:
        # Clean up
        if temp_path.exists():
            temp_path.unlink()


if __name__ == "__main__":
    test_find_notebooks()
    test_notebook_info()
    test_generate_html()
    print("\n✅ All gallery generator tests passed successfully!")
