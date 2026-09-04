from aiguard import redact


def test_redact():
    assert redact("api_key=secret123") == "api_key=[REDACTED]"
