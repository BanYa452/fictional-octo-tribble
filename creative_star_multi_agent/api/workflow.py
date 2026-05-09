
from fastapi import APIRouter
from pydantic import BaseModel

from agents.strategy_agent import StrategyAgent
from agents.topic_agent import TopicAgent
from agents.script_agent import ScriptAgent
from agents.rewrite_agent import RewriteAgent
from agents.review_agent import ReviewAgent
from agents.ops_agent import OpsAgent

router = APIRouter(prefix="/workflow", tags=["workflow"])

class WorkflowRequest(BaseModel):
    industry: str
    advantage: str
    audience: str
    goal: str

@router.post("/run")
def run_workflow(req: WorkflowRequest):

    strategy = StrategyAgent().run(
        f"行业:{req.industry}\n优势:{req.advantage}\n目标:{req.goal}"
    )

    topics = TopicAgent().run(strategy)

    script = ScriptAgent().run(topics)

    rewritten = RewriteAgent().run(script)

    review = ReviewAgent().run(rewritten)

    ops = OpsAgent().run(review)

    return {
        "strategy": strategy,
        "topics": topics,
        "script": script,
        "rewritten": rewritten,
        "review": review,
        "ops": ops
    }
