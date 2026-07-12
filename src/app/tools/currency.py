import requests
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from langchain.tools import tool

from config import EXCHANGE_API_KEY


def _convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Конвертирует сумму через публичный API [frankfurter.app](https://frankfurter.dev/)
    GET https://api.frankfurter.app/latest?from=USD&to=RUB
    --------- frankfurter не поддерживает конвертацию рубля, поэтому ExchangeRate.host --------

    GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/{from_currency}

    :amount: номинал в изначальнлой валюте
    :from_currency: аббревиатура изначальной валюты
    :to_currency: аббревиатура целевой валюты (RUB)

    :returns: номинал в целевой валюте; В случае ошибки конвертации возвращает -1
    """
    if from_currency == to_currency:
        return amount
    
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{from_currency}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            new_amount = data["conversion_rates"][to_currency] * amount
            return round(new_amount, 5)             # точность до 5 знака после запятой
        else:
            return -1

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return -1.0

@tool(description="Переводит номинал одной валюты в другую")
def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Transfer face value from one currency to another currency
    Args:
        amount:
            Face value in the original currency
        from_currency:
            The abbreviation of the original currency:
            - "RUB"
            - "USD"
            - "EUR"
            - "KZT"
            ...
        to_currency:
        The abbreviation of the new currency to convert the face value to:
            - "RUB"
            - "USD"
            - "EUR"
            - "KZT"
            ...        

    :returns:
        Calculate value in another currency
    """
    return _convert_currency(amount=amount, from_currency=from_currency, to_currency=to_currency)