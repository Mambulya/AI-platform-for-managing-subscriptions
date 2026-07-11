import sys
from pathlib import Path
root = str(Path(__file__).resolve().parent.parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)

from langchain.tools import tool

@tool
def finish_chat() -> None:
    """
    Finish the chat if the user clearly wishes to end the dialog
    """
    return "END_CHAT"