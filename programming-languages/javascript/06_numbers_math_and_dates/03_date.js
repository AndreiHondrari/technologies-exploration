"use strict";

function main() {
  console.log("** START **\n");

  // this has timezone offset applied (and date parts from now)
  console.log("# Date A");
  const d1 = new Date();
  console.log("DATE_A |", d1);
  console.log("TZ OFFSET |", d1.getTimezoneOffset());
  console.log("TSTR |", d1.toTimeString());
  console.log("UTCSTR |", d1.toUTCString());

  // this has timezone offset applied (and date parts from now)
  console.log("\n# Date B");
  const d2 = new Date(1999, 0, 3, 11, 22, 33, 120);
  console.log("DATE_B |", d2);
  console.log("TZ OFFSET |", d2.getTimezoneOffset());
  console.log("TSTR |", d2.toTimeString());
  console.log("UTCSTR |", d2.toUTCString());

  // this is precise date as specified
  console.log("\n# Date C");
  const d3 = new Date(Date.UTC(1999));
  console.log("DATE_C |", d3);
  console.log("TZ OFFSET |", d3.getTimezoneOffset());
  console.log("TSTR |", d3.toTimeString());
  console.log("UTCSTR |", d3.toUTCString());

  console.log("\n# UTC vs local");
  const d4 = new Date(new Date(1999, 0, 1, 0));
  console.log("ISO |", d4.toISOString());
  console.log("UTC |", d4.toUTCString());
  console.log("LOC |", d4.toLocaleString());
  console.log(d4.getHours());
  console.log(d4.getUTCHours());

  console.log("\n** END **");
}

main();
