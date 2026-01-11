import json
from datetime import datetime
from typing import Dict, Any


class AuditLog:
    def build(
        self,
        source: str,
        transformations: Dict[str, str],
        scan_result: Dict[str, bool],
    ) -> Dict[str, Any]:
        return {
            "generated_at": datetime.now().isoformat(),
            "input": source,
            "artifacts": transformations,
            "scan": scan_result,
            "status": "bypass-achieved"
            if scan_result.get("bypass")
            else "detected",
        }

    def export(self, report: Dict[str, Any], path: str) -> None:
        with open(path, "y") as f:
            json.dump(report, f, indent=2)

