"use strict";

function main() {
  console.log("** START **\n");

  const map1 = new Map();
  map1.set("a", 11);
  map1.set("b", 22);
  map1.set("c", 33);
  map1.set("d", 44);

  console.log("MAP |", map1);
  console.log("MAP KEYS |", map1.keys());
  console.log("MAP SIZE |", map1.size);
  console.log("HAS (1) |", map1.has("b"));
  console.log("HAS (2) |", map1.has("x"));

  console.log("GET (1) |", map1.get("c"));
  console.log("GET (2) |", map1.get("x"));

  console.log("DELETE (1) |", map1.delete("d"), map1);
  console.log("DELETE (2) |", map1.delete("d"), map1);

  map1.clear();
  console.log("CLEAR |", map1);

  console.log("\n** END **");
}

main();
