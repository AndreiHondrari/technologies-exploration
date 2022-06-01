"use strict";

function main() {
  console.log("** START **\n");

  const s1 = new Set();

  s1.add(11);
  s1.add(11);
  s1.add(11);
  s1.add(22);
  s1.add(22);
  s1.add(22);
  s1.add(22);
  s1.add(33);
  s1.add(66);
  s1.add(99);

  console.log("SET |", s1);
  console.log("HAS (1) |", s1.has(22));
  console.log("HAS (2) |", s1.has(44));
  console.log("VALUES |", s1.values());
  console.log("DELETE (1) |", s1.delete(33), s1);
  console.log("DELETE (2) |", s1.delete(11), s1);
  console.log("DELETE (3) |", s1.delete(77), s1);

  console.log("\n** END **");
}

main();
