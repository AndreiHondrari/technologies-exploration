"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = [11, 22, 33, 44, 55, 44, 55, 33, 22, 11];

  console.log("FIND |", arr1.find((v) => v > 30));
  console.log("FIND_INDEX |", arr1.findIndex((v) => v > 30));
  console.log("INDEX_OF |", arr1.indexOf(44));
  console.log("LAST_INDEX_OF |", arr1.lastIndexOf(33));

  console.log("\n** END **");
}

main();
