import requests


def post_result(webhook_url: str, ok: bool) -> int:
    """Send validation result to a webhook. No proxy configuration is used."""
    r = requests.post(webhook_url, json={"ok": ok}, timeout=5)
    return r.status_code
