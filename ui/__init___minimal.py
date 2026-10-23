"""Minimal fixed __init__.py for whisk.ui that avoids Python 2 syntax issues."""

# Don't import ui2 (has Python 2 syntax)
# Just make read, trace, whiskerdata accessible

__all__ = ["read", "trace", "whiskerdata"]
