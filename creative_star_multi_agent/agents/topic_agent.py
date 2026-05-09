
from agents.base_agent import BaseAgent

class TopicAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你是抖音选题专家，负责生成高播放视频选题。"
        )
