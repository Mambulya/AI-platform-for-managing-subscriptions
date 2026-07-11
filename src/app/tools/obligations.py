import json 
import sys
from pathlib import Path
root = str(Path(__file__).resolve().parent.parent.parent)
if root not in sys.path:
    sys.path.insert(0, root)

from langchain.tools import tool

from app.config import FILE_1


def _get_obligations(path:str=FILE_1, status:str=None, category:str=None) -> list:
    """
    Возвращает список финансовых обязательств пользователя. Данные читаются из локального JSON- файла
    Параметры status и category фильтруют возвращаемый список.
    :path: путь файла с информацией пользователя
    :status: статус подписки
    :category: категория трат

    :returns: список подписок пользователя
    """
    subscriptions = []
    with open(path, 'r') as file:
        all_subs = json.load(file)

        if status == None and category == None:
                subscriptions = all_subs
        else:
            if status == None and category != None:
                for sub in all_subs:
                    if sub["category"] == category:
                        subscriptions.append(sub)
            elif status != None and category == None:
                for sub in all_subs:
                    if sub["status"] == status:
                        subscriptions.append(sub)
            else:
                for sub in all_subs:
                    if sub["status"] == status and sub["category"] == category:
                          subscriptions.append(sub)
    return subscriptions

@tool(description=" Считывает информацию о подписках")
def get_obligations(status:str=None, category:str=None) -> list:
    """
    Get the inforamtion about the user's subscriptions
    Args:
        status:
            Status of subsctiption
            Possible values:
            - "active"
            - "deactivated"
        category:
            Category of subscribtion
    :returns:
        List of filtered by status and category subscriptions
    """
    return _get_obligations(status=status, category=category)