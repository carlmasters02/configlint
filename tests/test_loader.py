from configlint.loader import validate

GOOD = "service: api\nimage: ghcr.io/acme/api:1.2\nreplicas: 3\n"


def test_valid_manifest():
    assert validate(GOOD) == []


def test_missing_field():
    assert "missing field: image" in validate("service: api\nreplicas: 1\n")


def test_bad_replicas():
    assert "replicas must be an integer" in validate("service: a\nimage: b\nreplicas: lots\n")
