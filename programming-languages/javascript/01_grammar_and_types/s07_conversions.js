"use strict";

function main() {
  console.log("** START **\n");

  let x = parseInt("1234");
  let y = parseFloat("88.99");

  console.log("int from string |", x);
  console.log("float from string |", y);

  let z = parseInt("obviously this is not a number ...");
  console.log("...non-number from string |", z);

  console.log("\n** END **");
}

main();
