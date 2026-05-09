
from core.llm import ask_llm

class BaseAgent:

    name = "base"

    def __init__(self, system_prompt):
        self.system_prompt = system_prompt

    def run(self, user_input):
        return ask_llm(self.system_prompt, user_input)
