"""Top-level whisk package.

This is the Janelia whisker tracking package.
Submodules are under whisk.ui
"""

# Make ui subpackage accessible
# Import ui lazily to avoid initialization issues with old code
try:
    from . import ui
except Exception:
    pass  # ui will still be accessible as whisk.ui even if __init__ fails

__all__ = ["ui"]
