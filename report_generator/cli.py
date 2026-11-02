"""Command-line entry point."""
import argparse
from .scheduler import generate_once, run_daily

def main() -> None:
    parser = argparse.ArgumentParser(description="Automated API-to-PDF reporting tool")
    sub = parser.add_subparsers(dest="command", required=True)
    generate = sub.add_parser("generate", help="Fetch API data and generate a PDF now")
    generate.add_argument("--limit", type=int, default=50, help="Number of API records (default: 50)")
    generate.add_argument("--output", default="reports", help="Output directory")
    schedule = sub.add_parser("schedule", help="Run a daily scheduled report")
    schedule.add_argument("--limit", type=int, default=50)
    schedule.add_argument("--output", default="reports")
    schedule.add_argument("--hour", type=int, default=9, help="Local hour, 0-23")
    schedule.add_argument("--minute", type=int, default=0, help="Minute, 0-59")
    args = parser.parse_args()
    if args.command == "generate":
        path = generate_once(args.limit, args.output)
        print(f"Report created: {path}")
    else:
        if not 0 <= args.hour <= 23 or not 0 <= args.minute <= 59:
            parser.error("hour must be 0-23 and minute must be 0-59")
        run_daily(args.limit, args.output, args.hour, args.minute)

if __name__ == "__main__":
    main()
