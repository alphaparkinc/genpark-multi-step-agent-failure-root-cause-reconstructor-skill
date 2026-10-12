"""MCP server for Multi-Step Agent Failure Root-Cause Reconstructor."""
import sys
import json
from client import AgentFailureReconstructor

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "reconstruct_trajectory_failure",
                "description": "Isolates the root-cause failure step in a multi-step agent trajectory",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "steps": {"type": "array"}
                    },
                    "required": ["steps"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "reconstruct_trajectory_failure":
            steps = params.get("arguments", {}).get("steps", [])
            res = AgentFailureReconstructor.reconstruct_failure(steps)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
