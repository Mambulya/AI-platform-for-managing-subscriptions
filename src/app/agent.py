from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor

from config import LLM_ROUTE, GEMINI_4_API_KEY              # заменить на .env
from config import SYSTEM_PROMPT
from tools.obligations import get_obligations
from tools.currency import convert_currency
from tools.finish import finish_chat
from logger import Logger


logger = Logger()

LLM = ChatOpenAI(
    model=LLM_ROUTE,
    api_key=GEMINI_4_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    callbacks=[logger]
)
agent_tools = [get_obligations, convert_currency, finish_chat]
agent = create_agent(model=LLM,
                   tools=agent_tools,
                   system_prompt=SYSTEM_PROMPT)


# from langchain_openai import ChatOpenAI
# from langchain.agents import create_agent
# from langchain_classic.agents import AgentExecutor
# from langchain_gigachat.chat_models import GigaChat

# from config import GIGA_API_KEY              # заменить на .env
# from config import SYSTEM_PROMPT
# from tools.obligations import get_obligations
# from tools.currency import convert_currency
# from tools.finish import finish_chat
# from logger import Logger


# # giga = GigaChat(
# #    
# #     credentials=GIGACHAT_API_KEY,
# #     verify_ssl_certs=False,
# # )
# logger = Logger()

# LLM = GigaChat(credentials=GIGA_API_KEY,
#                verify_ssl_certs=False
#                )

# agent_tools = [get_obligations, convert_currency, finish_chat]
# agent = create_agent(model=LLM,
#                    tools=agent_tools,
#                    system_prompt=SYSTEM_PROMPT)


