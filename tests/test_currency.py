import sys
import os
from pathlib import Path
root = str(Path(__file__).resolve().parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)

import pytest

from app.tools.currency import _convert_currency