# AI-platform-for-managing-personal-subscriptions-and-regular-payments
MVP for Sber internship 



# 4 Архитектура проекта
Иерархия файлов соответствует следующей структуре:
```
|–––data
|    |–subscriptions_1.json
|    |–subscriptions_2.json
|    |–subscriptions_3.json
|–––src
|    |-app
|       |–__init__.py
|       |–tools
|           |–__init__.py
|           |–currency.py                  # convert_currency(amount, from_currency, to_currency)         
|           |–finish.py                    
|           |-obligations.py               # get_obligations(status, category)
|       |–agent.py
|       |–config.py
|       |–logger.py
|	    |–main.py
        |-subscription.py
|    |-tests
|       |–__init__.py
|       |-test_currency.py
|       |–test_obligations.py
|–––.env
|–––Dockerfile
|–––README.md
|–––requirements.txt
```