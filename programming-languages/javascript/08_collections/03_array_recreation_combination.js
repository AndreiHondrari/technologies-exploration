"use strict";

function main() {
  console.log("** START **\n");

  const arr1 = [11, 22, 33];
  const arr2 = [44, 55, 66];
  const arr3 = new Array(5);

  console.log("CONCAT |", arr1.concat(arr2));
  console.log("FROM |", Array.from(arr2));
  console.log("OF |", Array.of(77, 88, 99));
  console.log("FILL |", arr3.fill(99));

  console.log("\n** END **");
}

main();
