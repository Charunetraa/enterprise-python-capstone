import pytest
from report_generator.processor import summarize_records

def test_summary_counts_and_average():
    records = [{"userId": 1, "title": "abc"}, {"userId": 1, "title": "hello"}, {"userId": 2, "title": "xy"}]
    result = summarize_records(records)
    assert result["record_count"] == 3
    assert result["unique_users"] == 2
    assert result["average_title_length"] == 10 / 3
    assert result["records_by_user"] == {"1": 2, "2": 1}

def test_empty_records_rejected():
    with pytest.raises(ValueError):
        summarize_records([])
