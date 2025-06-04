# A simple Python script to demonstrate repository functionality


def greet(name: str) -> str:
    """Return a greeting for the specified name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Codex"

    print(greet(name))
