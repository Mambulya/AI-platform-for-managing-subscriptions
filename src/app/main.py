import openai
from agent import agent
from agent import Logger, logger
from config import YELLOW, RESET


LINE = 100
STOP_KEYWORDS = ("stop", "quit", "exit", "стоп", "выйти")

def write_in_frame(message:str):
    """
    Описывает сообщение, обведенное в рамку, в формате CLI

    :message: сообщение от модели или программы

    :returns: сообщение message в рамке
    """
    width = len(message) + 4
    print('-'*width)
    print("|", message, "|")
    print('-'*width)


if __name__ == "__main__":
    while True:
        user_message = input(f"{YELLOW}>>> ").strip()
        print(f"{RESET}")
        if not user_message:
            continue
        try:
            if any(stop_word in user_message.lower() for stop_word in STOP_KEYWORDS):
                write_in_frame(message="Чат закрыт")
                break
            response = agent.invoke({"messages":[{"role":"user", "content":user_message}]}, config={"callbacks": [logger]})
            last_message = response["messages"][-1]

            if logger.finish:
                write_in_frame(message="Чат закрыт")
                break
            else:
                print(last_message.content)
        except openai.RateLimitError as overloadError:                      
            write_in_frame(message="х Модель сейчас перегружена. Пожалуйста, попробуйте снова через несколько минут")
            break
        except TypeError as notInformedError:
            write_in_frame(message="x У модели нет достаточно сведений для этого запроса")
        except UnicodeEncodeError as unicodeError:
            write_in_frame(message="x Встретился символ, который не удается закодировать. Пожалуйста, перефразируйте вопрос")