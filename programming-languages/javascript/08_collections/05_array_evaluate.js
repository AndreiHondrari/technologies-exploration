"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100];

  console.log("EVERY (1) |", arr1.every((v) => v <= 100));
  console.log("EVERY (2) |", arr1.every((v) => v > 50));

  console.log("INCLUDES (1) |", arr1.includes(100));
  console.log("INCLUDES (2) |", arr1.includes(9999));

  console.log("SOME (1) |", arr1.some((v) => v % 3 == 0));
  console.log("SOME (2) |", arr1.some((v) => v > 100));

  console.log("\n** END **");
}

main();
