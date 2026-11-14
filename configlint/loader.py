import yaml

REQUIRED = ("service", "image", "replicas")


def load_manifest(text: str) -> dict:
    """Parse a user-submitted YAML deploy manifest."""
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("manifest must be a mapping")
    return data


def validate(text: str) -> list[str]:
    data = load_manifest(text)
    errors = [f"missing field: {k}" for k in REQUIRED if k not in data]
    if "replicas" in data and not isinstance(data["replicas"], int):
        errors.append("replicas must be an integer")
    return errors
