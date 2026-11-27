from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.forms = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.links.append(attrs)
        if tag == "form":
            self.forms.append(attrs)


class PublicOfferSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.brief = (ROOT / "brief.html").read_text(encoding="utf-8")

    def test_current_price_and_scope_are_unambiguous(self):
        self.assertIn("₹999", self.index)
        self.assertNotIn("₹499", self.index)
        self.assertIn("अधिकतम 500 शब्द", self.index)
        self.assertIn("एक consolidated revision", self.index)
        self.assertIn("2 working days", self.index)
        self.assertIn("30 नवम्बर 2026", self.index)

    def test_payment_is_after_written_scope(self):
        self.assertIn("लिखित scope", self.index)
        self.assertIn("भुगतान की पुष्टि के बिना काम शुरू नहीं होगा", self.index)
        self.assertIn("rzp.io/rzp/UhC1i8c", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_enquiry_brief_is_local_draft_not_auto_submission(self):
        parser = LinkParser()
        parser.feed(self.brief)
        self.assertTrue(parser.forms)
        self.assertIn("यह form आपके browser में ही विवरण तैयार करता है", self.brief)
        self.assertIn("wa.me/918082935186", self.brief)
        self.assertIn("mailto:sainirampaul60@gmail.com", self.brief)
        self.assertNotRegex(self.brief, r"\b(fetch|XMLHttpRequest)\s*\(")

    def test_external_new_tab_links_use_safe_rel(self):
        parser = LinkParser()
        parser.feed(self.index)
        for link in parser.links:
            if link.get("target") == "_blank":
                rel = set(link.get("rel", "").lower().split())
                self.assertTrue({"noopener", "noreferrer"}.issubset(rel), link)

    def test_required_public_files_exist(self):
        self.assertTrue((ROOT / "index.html").is_file())
        self.assertTrue((ROOT / "brief.html").is_file())


if __name__ == "__main__":
    unittest.main()
