"""Non-destructive secret redaction helpers."""

import re

_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key\s*[=:]\s*)[^\s,]+"),
    re.compile(r"(?i)(token\s*[=:]\s*)[^\s,]+"),
)


def redact(text: str, replacement: str = "[REDACTED]") -> str:
    """Redact common key/token assignments from text."""
    for pattern in _PATTERNS:
        text = pattern.sub(lambda match: match.group(1) + replacement, text)
    return text
