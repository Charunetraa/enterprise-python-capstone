"""Create a PDF report and a chart from processed records."""
from __future__ import annotations
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def create_report(records: list[dict], summary: dict, output_dir: str = "reports") -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    pdf_path = out / "automated_data_report.pdf"
    chart_path = out / "records_by_user.png"
    labels = list(summary["records_by_user"].keys())
    values = list(summary["records_by_user"].values())
    plt.figure(figsize=(7, 3.5))
    plt.bar(labels, values)
    plt.title("Records by User ID")
    plt.xlabel("User ID")
    plt.ylabel("Record count")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    plt.close()

    styles = getSampleStyleSheet()
    story = [Paragraph("Automated Data Report", styles["Title"]),
             Paragraph("Source: JSONPlaceholder public API", styles["Normal"]), Spacer(1, 12)]
    metrics = [["Metric", "Value"], ["Records retrieved", summary["record_count"]],
               ["Unique users", summary["unique_users"]],
               ["Average title length", summary["average_title_length"]]]
    table = Table(metrics, colWidths=[220, 180])
    table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#243b53")),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("PADDING", (0,0), (-1,-1), 8)]))
    story.extend([table, Spacer(1, 16), Image(str(chart_path), width=450, height=225), Spacer(1, 12)])
    story.append(Paragraph("Sample records", styles["Heading2"]))
    for row in records[:10]:
        story.append(Paragraph(f'{row.get("id", "")}. {row.get("title", "")}', styles["BodyText"]))
        story.append(Spacer(1, 4))
    SimpleDocTemplate(str(pdf_path), pagesize=letter, title="Automated Data Report").build(story)
    return pdf_path
