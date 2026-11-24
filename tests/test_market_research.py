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
            ("reminders.csv", "reminder_id"),
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
        _, coverage = read_csv("country-coverage.csv")
        countries = {row["country_or_territory"] for row in coverage}
        for row in opportunities:
            self.assertIn(row["organization_record_id"], organization_ids)
            self.assertIn(row["source_id"], source_ids)
            self.assertIn("countries_covered", row)
            covered = [country.strip() for country in row["countries_covered"].split(";") if country.strip()]
            self.assertTrue(covered, row["opportunity_id"])
            for country in covered:
                self.assertIn(country, countries, f"{row['opportunity_id']} {country}")
            self.assertTrue(valid_https(row["notice_url"]), row["opportunity_id"])
            valid_date(row["published_date"])
            valid_date(row["deadline"])
            self.assertIn("country_or_territory", row)
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
            "Hospital/health organization": "hospital_health",
            "Publisher/media": "publisher_media",
            "Education/training": "education_training",
            "Other": "other",
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


    def test_country_funnel_metrics_are_complete_and_reconciled(self):
        _, coverage = read_csv("country-coverage.csv")
        required = [
            "messages_delivered", "delivery_status_unknown", "bounces",
            "opt_outs_or_refusals", "follow_up_messages_sent", "follow_up_messages_delivered",
            "follow_up_delivery_status_unknown", "follow_up_bounces", "follow_up_replies",
            "quotes_issued", "payment_requests_issued", "payment_claims", "payment_claimed_inr",
            "verified_payment_transactions", "work_in_progress", "qa_passed", "support_open", "support_closed",
            "written_scopes_sent", "deliveries",
            "customer_acceptances", "repeat_purchases", "gross_revenue_inr",
            "fees_inr", "refunds_inr", "net_revenue_inr",
        ]
        numeric = [
            "organizations_identified", "qualified_for_current_sri_offer",
            "official_contacts_verified", "first_contacts_sent", "messages_delivered",
            "delivery_status_unknown", "bounces", "replies", "opt_outs_or_refusals",
            "follow_up_messages_sent", "follow_up_messages_delivered", "follow_up_delivery_status_unknown",
            "follow_up_bounces", "follow_up_replies", "buyer_enquiries", "written_scopes_sent",
            "quotes_issued", "accepted_orders", "payment_requests_issued", "payment_claims",
            "payment_claimed_inr", "verified_payment_transactions", "work_in_progress", "qa_passed", "support_open", "support_closed",
            "verified_payments_inr", "deliveries", "customer_acceptances",
            "repeat_purchases", "gross_revenue_inr", "fees_inr", "refunds_inr",
            "net_revenue_inr",
        ]
        for row in coverage:
            for key in required:
                self.assertIn(key, row, row["country_or_territory"])
            for key in numeric:
                self.assertGreaterEqual(int(row[key]), 0, f"{row['country_or_territory']} {key}")
            self.assertEqual(
                int(row["messages_delivered"]) + int(row["delivery_status_unknown"]) + int(row["bounces"]),
                int(row["first_contacts_sent"]),
                row["country_or_territory"],
            )
            self.assertEqual(
                int(row["follow_up_messages_delivered"]) + int(row["follow_up_delivery_status_unknown"]) + int(row["follow_up_bounces"]),
                int(row["follow_up_messages_sent"]),
                row["country_or_territory"],
            )
            self.assertEqual(
                int(row["verified_payments_inr"]),
                int(row["gross_revenue_inr"]),
                row["country_or_territory"],
            )
            self.assertEqual(
                int(row["net_revenue_inr"]),
                int(row["gross_revenue_inr"]) - int(row["fees_inr"]) - int(row["refunds_inr"]),
                row["country_or_territory"],
            )

    def test_organization_country_pairs_are_deduplicated(self):
        _, organizations = read_csv("organizations.csv")
        pairs = [
            (row["country_or_territory"].strip().casefold(), row["organization"].strip().casefold())
            for row in organizations
        ]
        self.assertEqual(len(pairs), len(set(pairs)))


    def test_reminders_reference_known_opportunities_and_do_not_authorize_unsolicited_contact(self):
        _, opportunities = read_csv("opportunities.csv")
        opportunity_ids = {row["opportunity_id"] for row in opportunities}
        _, reminders = read_csv("reminders.csv")
        for row in reminders:
            self.assertEqual(row["related_record_type"], "opportunity")
            self.assertIn(row["related_record_id"], opportunity_ids)
            valid_date(row["due_date"])
            valid_date(row["last_checked"])
            self.assertTrue(row["action"].strip())
            self.assertTrue(row["permission_basis"].strip())
            self.assertIn(row["external_contact_allowed"], {"YES", "NO"})
            self.assertEqual(row["external_contact_allowed"], "NO")


    def test_readme_checkpoint_counts_match_register(self):
        readme = (DATA / "README.md").read_text(encoding="utf-8")
        _, sources = read_csv("sources.csv")
        _, organizations = read_csv("organizations.csv")
        _, opportunities = read_csv("opportunities.csv")
        _, coverage = read_csv("country-coverage.csv")
        _, reminders = read_csv("reminders.csv")
        expected = [
            f"**{len(coverage)} country rows**",
            f"**{len(organizations)} organization records**",
            f"**{len(opportunities)} procurement opportunities**",
            f"**{len(sources)} dated sources**",
            f"**{len(reminders)} internal reminders**",
        ]
        for phrase in expected:
            self.assertIn(phrase, readme, phrase)


if __name__ == "__main__":
    unittest.main()
