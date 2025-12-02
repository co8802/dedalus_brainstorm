from collections import defaultdict
from typing import List, DefaultDict

class Memory:
    """Super simple in-memory store: topic -> list of ideas."""
    def __init__(self) -> None:
        self._ideas: DefaultDict[str, List[str]] = defaultdict(list)

    def add_idea(self, topic: str, idea: str) -> None:
        self._ideas[topic].append(idea)

    def get_ideas(self, topic: str) -> List[str]:
        # return a copy so callers can't mutate our internal list
        return list(self._ideas[topic])
