import csv
import json
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def summarize(rows):
    if not rows:
        raise ValueError("Empty fixture")
    ids = [r["Booking ID"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate booking ID")
    values = []
    for row in rows:
        try:
            value = Decimal(row["Booking Value"])
        except (InvalidOperation, KeyError):
            raise ValueError("Missing or non-numeric value")
        if not value.is_finite():
            raise ValueError("Non-finite value")
        values.append(value)
    success = [v for r, v in zip(rows, values) if r["Booking Status"] == "Success"]
    return {
        "total_data_rows": len(rows),
        "booking_status_counts": dict(Counter(r["Booking Status"] for r in rows)),
        "booking_value_sum": float(sum(values)),
        "booking_value_mean_all_rows": float(sum(values) / len(values)),
        "successful_booking_count": len(success),
        "successful_booking_value_mean": float(sum(success) / len(success)) if success else None,
    }

def load_rows():
    with (ROOT / "data/synthetic-bookings.csv").open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    actual = summarize(load_rows())
    expected = json.loads((ROOT / "data/expected-summary.json").read_text())
    if actual != expected:
        raise SystemExit("Fixture expectations do not match")
    print(json.dumps({"fixture": "passed", "summary": actual}, indent=2))
