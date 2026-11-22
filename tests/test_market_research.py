import csv
import datetime as dt
import unittest
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "market-research"


def read_csv(name):
    with (DATA / name).open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise AssertionError(f"{name}: missing or duplicate headers")
        if any(None in row for row in rows):
            raise AssertionError(f"{name}: row has more values than its header")
        return reader.fieldnames, rows


def valid_date(value):
    dt.date.fromisoformat(value)


def valid_https(value):
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


class MarketResearchRegisterTests(unittest.TestCase):
    def test_required_files_and_unique_ids(self):
        for filename, key in [
            ("sources.csv", "source_id"),
            ("organizations.csv", "record_id"),
            ("opportunities.csv", "opportunity_id"),
        ]:
            _, rows = read_csv(filename)
            values = [row[key] for row in rows]
            self.assertTrue(rows, filename)
            self.assertEqual(len(values), len(set(values)), filename)
            self.assertTrue(all(values), filename)

    def test_source_records_are_dated_and_linked(self):
        _, rows = read_csv("sources.csv")
        for row in rows:
            valid_date(row["access_date"])
            self.assertTrue(valid_https(row["source_url"]), row["source_id"])
            self.assertTrue(row["source_name"].strip())

    def test_organization_records_have_evidence_and_valid_sources(self):
        _, sources = read_csv("sources.csv")
        source_ids = {row["source_id"] for row in sources}
        _, organizations = read_csv("organizations.csv")
        for row in organizations:
            valid_date(row["source_date"])
            valid_date(row["last_checked"])
            self.assertTrue(valid_https(row["official_source_url"]), row["record_id"])
            self.assertTrue(row["observed_need_or_signal"].strip(), row["record_id"])
            self.assertTrue(row["fit_assessment"].strip(), row["record_id"])
            self.assertTrue(row["outreach_eligibility"].strip(), row["record_id"])
            if row["public_business_channel"].strip():
                self.assertTrue(valid_https(row["channel_source_url"]), row["record_id"])
            for source_id in row["channel_source_url"].split(";"):
                if source_id.startswith("SRC-"):
                    self.assertIn(source_id, source_ids)

    def test_opportunities_reference_existing_organizations_and_sources(self):
        _, sources = read_csv("sources.csv")
        source_ids = {row["source_id"] for row in sources}
        _, organizations = read_csv("organizations.csv")
        organization_ids = {row["record_id"] for row in organizations}
        _, opportunities = read_csv("opportunities.csv")
        for row in opportunities:
            self.assertIn(row["organization_record_id"], organization_ids)
            self.assertIn(row["source_id"], source_ids)
            self.assertTrue(valid_https(row["notice_url"]), row["opportunity_id"])
            valid_date(row["published_date"])
            valid_date(row["deadline"])
            self.assertTrue(row["scope_summary"].strip())
            self.assertTrue(row["capability_gaps"].strip())
            self.assertTrue(row["decision"].strip())

    def test_country_totals_match_organization_register(self):
        _, organizations = read_csv("organizations.csv")
        _, sources = read_csv("sources.csv")
        source_ids = {row["source_id"] for row in sources}
        _, coverage = read_csv("country-coverage.csv")
        segment_columns = {
            "Government/public": "government_or_public",
            "Private company": "private_company",
            "NGO/nonprofit": "ngo_nonprofit",
            "University/research lab": "university_research_lab",
            "Intergovernmental organization": "international_organization",
        }
        for country in coverage:
            for source_id in country["evidence_source_ids"].split(";"):
                self.assertIn(source_id, source_ids, country["country_or_territory"])
            records = [r for r in organizations if r["country_or_territory"] == country["country_or_territory"]]
            unique_orgs = {r["organization"] for r in records}
            self.assertEqual(int(country["organizations_identified"]), len(unique_orgs), country["country_or_territory"])
            for segment, column in segment_columns.items():
                expected = len({r["organization"] for r in records if r["institution_segment"] == segment})
                self.assertEqual(int(country[column]), expected, f"{country['country_or_territory']} {column}")
            self.assertEqual(
                int(country["official_contacts_verified"]),
                len({r["organization"] for r in records if r["public_business_channel"].strip()}),
                country["country_or_territory"],
            )
            for key in ("qualified_for_current_sri_offer", "first_contacts_sent", "replies", "buyer_enquiries", "accepted_orders", "verified_payments_inr"):
                self.assertGreaterEqual(int(country[key]), 0, f"{country['country_or_territory']} {key}")
            if int(country["verified_payments_inr"]) > 0:
                self.assertGreater(int(country["accepted_orders"]), 0)


if __name__ == "__main__":
    unittest.main()
