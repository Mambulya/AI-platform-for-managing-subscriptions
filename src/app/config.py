from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# ключи LLM
GEMINI_4_API_KEY = os.getenv("GEMINI_4_API_KEY")
LLM_ROUTE = os.getenv("LLM_ROUTE")
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

SYSTEM_PROMPT = """
You are a subscriptions manager. You need to consider subscribtions regarding their attributes, such as category, next_payment_day, status, currency, amount, and title. 
To compare prices of different subscriptions, use the tool that is called convert_currency.
Default currency to display is RUB.
If there is a need to compare prices, consider all subscriptions and convert all prices into RUB (if the user did not mention another currency).
If convert_currency returned the number less than 0, something went wrong. Inform the user about it.
Reason step-by-step using thoughts before selecting tools.
Write your answers in CLI format. There is no need to use Markdown style.
If a user wants to end the chat, use the tool that is called as finish_chat.
A user want to know how to optimize the expenses.
If it was impossible to respond, there was not enough data or an external API was unavailable, explicitly report it. Do not mislead the user.
"""

# тестирующие json-файлы
FILE_1 = PROJECT_ROOT / "data/subscriptions_1.json"
FILE_2 = PROJECT_ROOT / "data/subscriptions_2.json"
FILE_3 = PROJECT_ROOT / "data/subscriptions_3.json"

# цвета терминала
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
