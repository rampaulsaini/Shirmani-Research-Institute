const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const html = fs.readFileSync("businessflow-lab.html", "utf8");
const start = html.indexOf("<script>") + "<script>".length;
const end = html.indexOf("</script>", start);
const script = html.slice(start, end);

test("inline application JavaScript parses", () => {
  assert.ok(start >= 8 && end > start, "inline script exists");
  assert.doesNotThrow(() => new vm.Script(script));
});
test("new records cannot be marked paid at creation", () => {
  const startForm = html.indexOf('<select id="stage">');
  const endForm = html.indexOf("</select>", startForm);
  const stageOptions = html.slice(startForm, endForm);
  assert.ok(startForm >= 0 && endForm > startForm);
  assert.equal(stageOptions.includes('value="paid"'), false);
});
test("paid state requires explicit external-account confirmation", () => {
  assert.ok(html.includes("वास्तविक बैंक/भुगतान खाते में इस invoice की पूरी राशि जमा होना स्वयं जाँच लिया हो"));
  assert.ok(html.includes("owner-confirmed-external-account-credit"));
});
test("CSV export neutralizes spreadsheet formula prefixes", () => {
  assert.ok(html.includes("function csvCell"));
  assert.ok(html.includes("s=\"'\"+s"));
});
test("date comparisons use local calendar date, not UTC ISO date", () => {
  const dateFn = html.slice(html.indexOf("const localDate="), html.indexOf("const validDate="));
  assert.ok(dateFn.includes("getFullYear") && dateFn.includes("getMonth") && dateFn.includes("getDate"));
  assert.equal(dateFn.includes("toISOString"), false);
});
test("storage failures are visible and empty backup is blocked", () => {
  assert.ok(html.includes("Browser storage में लिखना विफल हुआ"));
  assert.ok(html.includes("डेटा पढ़ा नहीं जा सका; खाली backup बनाकर पुराने डेटा को overwrite न करें"));
});
test("rendered customer fields are HTML escaped", () => {
  assert.ok(html.includes("const esc=s=>String"));
  assert.ok(html.includes("esc(r.customer)"));
});

test("enquiry brief discloses pilot price, scope, and delivery conditions", () => {
  const brief = fs.readFileSync("brief.html", "utf8");
  assert.ok(brief.includes("₹499"));
  assert.ok(brief.includes("30 नवम्बर 2026 तक"));
  assert.ok(brief.includes("अधिकतम 500 शब्द"));
  assert.ok(brief.includes("एक consolidated revision"));
  assert.ok(brief.includes("भुगतान की पुष्टि"));
  assert.ok(brief.includes("No subscription"));
  assert.ok(brief.includes("Pilot offer (30 Nov 2026 tak)"));
});

test("calendar validation rejects impossible dates and accepts leap days", () => {
  const match = script.match(/function validDate\\(s\\)\\{[\\s\\S]*?\\n\\}/);
  assert.ok(match, "validDate helper exists");
  const validDate = vm.runInNewContext("(" + match[0] + ")");
  assert.equal(validDate("2024-02-29"), true);
  assert.equal(validDate("2025-02-29"), false);
  assert.equal(validDate("2026-02-31"), false);
  assert.equal(validDate("2026-13-01"), false);
});
test("stored paid records require owner-confirmation metadata and unique IDs", () => {
  assert.ok(html.includes('r.paymentCheck==="owner-confirmed-external-account-credit"'));
  assert.ok(html.includes("new Set(parsed.map(x=>x.id)).size!==parsed.length"));
  assert.ok(html.includes('"paymentCheck"'));
});
