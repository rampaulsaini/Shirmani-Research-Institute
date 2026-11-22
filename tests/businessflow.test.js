const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

const html = fs.readFileSync("businessflow-lab.html", "utf8");
const match = html.match(/<script>([\\s\\S]*?)<\\/script>/);
test("inline application JavaScript parses", () => {
  assert.ok(match, "inline script exists");
  assert.doesNotThrow(() => new vm.Script(match[1]));
});
test("new records cannot be marked paid at creation", () => {
  const form = html.match(/<select id="stage">([\\s\\S]*?)<\\/select>/);
  assert.ok(form);
  assert.doesNotMatch(form[1], /value=["']paid["']/);
});
test("paid state requires explicit external-account confirmation", () => {
  assert.match(html, /वास्तविक बैंक\/भुगतान खाते में इस invoice की पूरी राशि जमा होना स्वयं जाँच लिया हो/);
  assert.match(html, /owner-confirmed-external-account-credit/);
});
test("CSV export neutralizes spreadsheet formula prefixes", () => {
  assert.match(html, /function csvCell/);
  assert.match(html, /\\[\\s\\u0000-\\u001f\\]\\*\\[=+@\\-\\]/);
});
test("date comparisons use local calendar date, not UTC ISO date", () => {
  assert.match(html, /function localDate/);
  assert.doesNotMatch(html.match(/function localDate\\(\\)[\\s\\S]*?\\n/)[0], /toISOString/);
});
test("storage failures are visible and empty backup is blocked", () => {
  assert.match(html, /Browser storage में लिखना विफल हुआ/);
  assert.match(html, /डेटा पढ़ा नहीं जा सका; खाली backup बनाकर पुराने डेटा को overwrite न करें/);
});
test("rendered customer fields are HTML escaped", () => {
  assert.match(html, /const esc=s=>String/);
  assert.match(html, /esc\(r.customer\)/);
});
