
from agents.base_agent import BaseAgent

class ScriptAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "你是短视频脚本专家，生成完整口播和镜头脚本。"
        )
