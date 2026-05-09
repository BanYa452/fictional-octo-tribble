
from agents.base_agent import BaseAgent

class StrategyAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你是短视频定位专家，负责输出账号定位、人设、风格。"
        )
