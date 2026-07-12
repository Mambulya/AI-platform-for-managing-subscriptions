from typing import TypedDict
from dataclasses import dataclass

@dataclass
class Subsctiption(TypedDict):
    id: str
    title: str
    amount: float
    currency: str
    category: str
    next_payment_date: str
    status: str