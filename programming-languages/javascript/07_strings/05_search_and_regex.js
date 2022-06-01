"use strict";

function main() {
  console.log("** START **\n");

  const msg = "Funny butterflies 123777aaa999 leonardos kekus";
  const expr1 = /[a-z]+/;
  const expr2 = /[a-z]+/g;
  const expr3 = /([a-z]+)/ig;

  console.log(" \n# match A |", msg.match(expr1));
  console.log(" \n# match B |", msg.match(expr2));
  console.log(" \n# match C |", msg.match(expr3));

  try {
    console.log(" \n# matchAll A |", msg.matchAll(expr1));
  } catch (e) {
    console.error("Caught intentionally |", String(e));
  }

  const result = msg.matchAll(expr2);
  console.log(" \n# matchAll B |", result);
  console.log([...result]);

  console.log("\n** END **");
}

main();
