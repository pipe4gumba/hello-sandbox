"""A greeting. That is the entire library."""

__all__ = ["greet"]


def greet(name: str = "world") -> str:
    """Return a greeting for ``name``.

    An empty or whitespace-only name falls back to ``world``.
    """
    name = name.strip() or "world"
    return f"Hello, {name}!"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
