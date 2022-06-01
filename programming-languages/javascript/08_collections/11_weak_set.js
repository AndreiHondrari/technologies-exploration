"use strict";

function main() {
  console.log("** START **\n");

  const weakSet1 = new WeakSet();

  const o1 = { a: 11 };
  const o2 = { b: 22 };
  const o3 = { c: 88 };

  weakSet1.add(o1);
  weakSet1.add(o1);
  weakSet1.add(o1);
  weakSet1.add(o2);
  weakSet1.add(o2);

  console.log("WEAK_SET |", weakSet1);
  console.log("HAS (1) |", weakSet1.has(o1));
  console.log("HAS (2) |", weakSet1.has(o3));

  console.log("\n** END **");
}

main();
