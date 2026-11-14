import sys
from .loader import validate


def main() -> int:
    errors = validate(sys.stdin.read())
    for e in errors:
        print(e)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
