
from agents.base_agent import BaseAgent

class OpsAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你是运营分析 Agent，负责生成发布时间和运营建议。"
        )
