"""Data cleaning and summary calculations."""
from collections import Counter

def summarize_records(records: list[dict]) -> dict:
    if not records:
        raise ValueError("No records were provided")
    user_counts = Counter(str(row.get("userId", "unknown")) for row in records)
    title_lengths = [len(str(row.get("title", ""))) for row in records]
    return {
        "record_count": len(records),
        "unique_users": len(user_counts),
        "average_title_length": round(sum(title_lengths) / len(title_lengths), 2),
        "records_by_user": dict(sorted(user_counts.items(), key=lambda item: int(item[0]) if item[0].isdigit() else 0)),
        "titles": [str(row.get("title", "")) for row in records],
    }
