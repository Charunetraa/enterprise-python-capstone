"""Simple recurring report scheduler."""
from apscheduler.schedulers.blocking import BlockingScheduler
from .api import fetch_records
from .processor import summarize_records
from .pdf_report import create_report

def generate_once(limit: int = 50, output_dir: str = "reports") -> str:
    records = fetch_records(limit=limit)
    summary = summarize_records(records)
    path = create_report(records, summary, output_dir=output_dir)
    return str(path)

def run_daily(limit: int = 50, output_dir: str = "reports", hour: int = 9, minute: int = 0) -> None:
    scheduler = BlockingScheduler()
    scheduler.add_job(generate_once, "cron", hour=hour, minute=minute,
                      kwargs={"limit": limit, "output_dir": output_dir}, id="daily_pdf_report",
                      max_instances=1, coalesce=True)
    print(f"Daily report scheduled for {hour:02d}:{minute:02d}. Press Ctrl+C to stop.")
    scheduler.start()
