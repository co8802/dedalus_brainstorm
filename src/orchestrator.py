from typing import Dict, Any, List
from memory import Memory
from agents import CreativeAgent, CriticalAgent, ImplementerAgent

class RoundManager:
    def __init__(self):
        self.mem = Memory()
        self.creative = CreativeAgent()
        self.critical = CriticalAgent()
        self.impl = ImplementerAgent()

    def run(self, topic: str) -> Dict[str, Any]:
        ideas = self.creative.respond(topic)
        for i in ideas:
            self.mem.add_idea(topic, i)
        ranked = self.critical.score(ideas)
        best, best_score = ranked[0]
        plan = self.impl.plan(best)
        return {
            "topic": topic,
            "ideas": ideas,
            "ranked": [{"idea": i, "score": s} for i, s in ranked],
            "chosen": {"idea": best, "score": best_score},
            "plan": plan,
        }
