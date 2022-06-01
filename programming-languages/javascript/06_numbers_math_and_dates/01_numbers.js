"use strict";

function main() {
  console.log("** START **\n");

  console.log("# Enumerate Number predefined values");
  for (const prop of Object.getOwnPropertyNames(Number)) {
    const thing = Number[prop];
    if (typeof (thing) === "number") {
      console.log(`Number.${prop} = ${thing}`);
    }
  }

  console.log("\n# Number evaluations");
  console.log("isInteger A |", Number.isInteger(123));
  console.log("isInteger B |", Number.isInteger(123.444));

  console.log("isFinite A |", Number.isFinite(123));
  console.log("isFinite B |", Number.isFinite(Number.POSITIVE_INFINITY));
  console.log("isFinite C |", Number.isFinite(Number.NEGATIVE_INFINITY));
  console.log("isFinite D |", Number.isFinite(Number.NaN));

  console.log("\n** END **");
}

main();
