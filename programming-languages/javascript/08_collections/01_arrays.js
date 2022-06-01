"use strict";

function main() {
  console.log("** START **\n");

  console.log("# Create simply");
  const arr1 = [];
  arr1.push(11);
  arr1.push(22);
  arr1.push(33);
  console.log("ARR1 |", arr1);

  const arr2 = new Array(0);
  arr2.push(44);
  arr2.push(55);
  arr2.push(66);
  console.log("ARR2 |", arr2);

  const arr3 = new Array(2);
  console.log("ARR3 (1) |", arr3);
  arr3[0] = 77;
  arr3[1] = 88;
  arr3[2] = 99;
  console.log("ARR3 (2) |", arr3);

  console.log("\n** END **");
}

main();
