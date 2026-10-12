"""Multi-Step Agent Failure Root-Cause Reconstructor.
100% Python Standard Library.
"""

class AgentFailureReconstructor:
    """Reconstructs the root-cause step in a multi-step agent trajectory where cascading errors originated."""

    @staticmethod
    def reconstruct_failure(steps: list) -> dict:
        root_cause_step = None
        cascading_failures = 0

        for idx, st in enumerate(steps):
            status = st.get("status", "ok").lower()
            err = st.get("error", "")
            if status in ("error", "failed", "timeout"):
                if root_cause_step is None:
                    root_cause_step = {
                        "step_index": idx,
                        "tool": st.get("tool", "unknown"),
                        "error_message": err,
                        "remediation_hint": "Retry with backoff or switch fallback provider" if "timeout" in err.lower() else "Validate tool input schema before invocation"
                    }
                else:
                    cascading_failures += 1

        return {
            "trajectory_healthy": root_cause_step is None,
            "root_cause": root_cause_step,
            "cascading_error_count": cascading_failures
        }
