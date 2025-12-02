from orchestrator import RoundManager
import json

if __name__ == "__main__":
    rm = RoundManager()
    result = rm.run("campus study-planner")
    print(json.dumps(result, indent=2))
