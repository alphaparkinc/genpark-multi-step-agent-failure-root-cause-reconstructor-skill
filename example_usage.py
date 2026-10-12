"""Example usage for Multi-Step Agent Failure Root-Cause Reconstructor."""
from client import AgentFailureReconstructor

if __name__ == "__main__":
    steps = [
        {"tool": "auth_check", "status": "ok"},
        {"tool": "fetch_orders", "status": "timeout", "error": "Upstream gateway timeout"},
        {"tool": "parse_orders", "status": "error", "error": "Null payload received"}
    ]
    res = AgentFailureReconstructor.reconstruct_failure(steps)
    print("Root Cause:", res["root_cause"])
