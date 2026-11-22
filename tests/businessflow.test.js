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
