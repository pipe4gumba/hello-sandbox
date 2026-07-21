# hello-sandbox

A deliberately boring greeting library.

This repository exists as a stable, public target for automation experiments —
CI runs, pull-request flows, merge settings. The code is intentionally trivial
and is not meant to be useful. Nothing here is a real product.

```python
from hello import greet

greet("world")  # "Hello, world!"
```

## Development

```bash
uv sync
uv run pytest -q
```

## Layout

| Path | Purpose |
|---|---|
| `src/hello.py` | The whole library: one function. |
| `tests/` | Tests for that one function. |
| `docs/` | Prose about the library. Safe to edit. |
