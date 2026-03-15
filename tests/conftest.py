"""Shared test configuration."""

import sys
from pathlib import Path

# handlers/ uses bare imports (e.g. `from decorators import …`),
# so we add it to sys.path for test discovery.
_handlers_dir = str(Path(__file__).resolve().parent.parent / "handlers")
if _handlers_dir not in sys.path:
    sys.path.insert(0, _handlers_dir)
