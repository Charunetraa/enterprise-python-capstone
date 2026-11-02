"""Fetch sample business-style records from a public API."""
from __future__ import annotations
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_records(limit: int = 50, timeout: int = 20) -> list[dict]:
    """Fetch up to *limit* sample records from JSONPlaceholder."""
    if limit < 1:
        raise ValueError("limit must be at least 1")
    response = requests.get(API_URL, params={"_limit": limit}, timeout=timeout)
    response.raise_for_status()
    data = response.json()
    if not isinstance(data, list):
        raise ValueError("API returned an unexpected response format")
    return data
