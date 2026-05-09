
from agents.base_agent import BaseAgent

class RewriteAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你负责优化文案，强化冲突感、节奏感和转化率。"
        )
