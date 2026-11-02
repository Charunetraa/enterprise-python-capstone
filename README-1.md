# Enterprise Python Automation Capstone

An end-to-end Python application that retrieves public API data, processes it, creates a PDF report with a chart, and supports daily scheduled execution.

## Features

- Retrieves sample records from the JSONPlaceholder REST API
- Calculates record count, unique users, average title length, and records per user
- Generates a PDF report and a PNG chart
- Provides a command-line interface using `argparse`
- Supports daily scheduling with APScheduler
- Includes unit tests and package configuration

## Architecture

```text
Command line (argparse)
        |
        v
API client (requests) ---> JSONPlaceholder API
        |
        v
Data processor (summary metrics)
        |
        v
PDF report + chart (ReportLab + Matplotlib)
        |
        v
reports/ output folder

Scheduler (APScheduler) ---> invokes the same report pipeline daily
```

## Requirements

- Python 3.10 or newer
- Internet connection for API retrieval

## Install

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\python.exe -m pip install -e .[test]
# macOS/Linux:
# .venv/bin/python -m pip install -e '.[test]'
```

If shell quoting causes issues, install dependencies with `python -m pip install -r requirements.txt`.

## Usage

Generate a report immediately:

```bash
capstone-report generate --limit 50 --output reports
```

Or run without installing the CLI command:

```bash
python -m report_generator.cli generate --limit 50
```

Schedule a report every day at 9:00 AM local machine time:

```bash
capstone-report schedule --hour 9 --minute 0
```

The scheduler must remain running for the scheduled job to execute. Press `Ctrl+C` to stop it.

## Output

- `reports/automated_data_report.pdf` — report with metrics, chart, and sample records
- `reports/records_by_user.png` — chart used in the report

## Tests

```bash
python -m pytest -q
```

## API and data note

This project uses JSONPlaceholder, a public demo REST API. Its records are sample data intended for development and demonstration, not live business information.

## Project layout

```text
report_generator/   Application package
  api.py            API retrieval
  processor.py      Data processing and summary metrics
  pdf_report.py     PDF and chart generation
  scheduler.py      Report pipeline and daily scheduler
  cli.py            Command-line interface
tests/              Unit tests
pyproject.toml      Package/build configuration
requirements.txt    Dependencies
```

## Capstone demonstration checklist

1. Install the project.
2. Run the `generate` command and show the generated PDF.
3. Show the chart and summary metrics in the report.
4. Run the unit tests.
5. Explain the scheduler command and that the process must remain running.
6. Show the public GitHub repository.

## License

MIT
