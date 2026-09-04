# aiguard

Non-destructive redaction of common API-key and token assignments before logs are stored or displayed.

```python
from aiguard import redact
safe = redact("api_key=example")
```

Run `pytest` to test. License: MIT.

Built by meduuv. `guns.lol/meduu`
