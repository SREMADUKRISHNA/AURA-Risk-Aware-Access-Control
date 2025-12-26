from config import settings

class DeviceFingerprint:
    """
    Evaluates the trustworthiness of the device and network context.
    """

    def evaluate(self, device_id: str, ip_address: str) -> float:
        """
        Calculate device risk score (0-100).
        """
        score = 50.0 # Default to neutral/unknown risk

        # 1. Check for Trusted Device naming convention
        if device_id.startswith(settings.TRUSTED_DEVICE_PREFIX):
            score -= 40.0 # High trust
        else:
            score += 20.0 # Unknown device penalty

        # 2. IP Address Checks (Simple Heuristics)
        if ip_address == "127.0.0.1" or ip_address.startswith("192.168."):
            score -= 10.0 # Local/Private network bonus
        else:
            score += 10.0 # Public/Unknown IP penalty

        return min(max(score, 0.0), 100.0)
