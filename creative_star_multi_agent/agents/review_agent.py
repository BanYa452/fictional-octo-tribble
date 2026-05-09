
from agents.base_agent import BaseAgent

class ReviewAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你是内容审核 Agent，负责检查重复表达和违规词。"
        )
