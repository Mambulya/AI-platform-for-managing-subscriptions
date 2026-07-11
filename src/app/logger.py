import json
from langchain_core.callbacks import BaseCallbackHandler

from config import BLUE, RESET

class Logger(BaseCallbackHandler):
    def __init__(self):
        self.finish = False

    def on_llm_start(self, serialized, prompts, *, run_id, parent_run_id = None, tags = None, metadata = None, **kwargs) -> None:
        print(f"{BLUE}[Thought] Модель анализирует запрос пользователя {RESET}")
    

    def on_tool_start(self, serialized, input_str, *, run_id, parent_run_id = None, tags = None, metadata = None, inputs = None, **kwargs) -> None:
        if serialized["name"] == "finish_chat":
            self.finish = True
        if serialized["name"] == "get_obligations":
            status = inputs.get("status") if inputs else None
            category = inputs.get("category") if inputs else None
            print(f'{BLUE}[Action] {serialized['name']}("status" : {status}, "category" : {category}){RESET}')
        else:
            print(f'{BLUE}[Action] {serialized['name']}({inputs}){RESET}')
   
    
    def on_tool_end(self, output, *, run_id, parent_run_id = None, **kwargs) -> None:
        print(f"{BLUE}[Observation] {output.content}{RESET}")



        