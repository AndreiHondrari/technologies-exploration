"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = { a: 11, b: 22 };
  const obj2 = { b: 44, x: 33 };

  const result = Object.assign(obj1, obj2);
  console.log("TARGET |", obj1);
  console.log("SOURCE |", obj2);
  console.log("RESULT |", result);

  console.log("\n** END **");
}

main();
