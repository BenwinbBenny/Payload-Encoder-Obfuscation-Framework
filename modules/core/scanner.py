class ThreatScanner:
    def __init__(self):
        # Generic operational indicators (not command names)
        self.patterns = [
            "admin_login",
            "config_update",
            "debug_mode",
            "auth_token",
            "service_restart",
        ]

        # Generic high-risk action words
        self.flags = [
            "override",
            "bypass",
            "elevate",
            "inject",
        ]

    def scan(self, text: str) -> bool:
        data = text.lower()
        return any(p in data for p in self.patterns + self.flags)

    def compare(self, raw: str, transformed: str) -> dict:
        raw_hit = self.scan(raw)
        masked_hit = self.scan(transformed)

        return {
            "raw_flagged": raw_hit,
            "masked_flagged": masked_hit,
            "bypass": raw_hit and not masked_hit,
        }
