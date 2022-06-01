"use strict";

function main() {
  console.log("** START **\n");

  const weak1 = new WeakMap();

  const o1 = { a: 11 };
  const o2 = { b: 22 };
  const o3 = { c: 88 };

  weak1.set(o1, { x: 333 });
  weak1.set(o2, { x: 444 });

  console.log("WEAK_MAP |", weak1);
  console.log("GET |", weak1.get(o2));
  console.log("HAS (1) |", weak1.has(o1));
  console.log("HAS (2) |", weak1.has(o3));

  console.log("\n** END **");
}

main();
