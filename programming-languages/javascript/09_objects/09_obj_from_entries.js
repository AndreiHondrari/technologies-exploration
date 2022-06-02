"use strict";

function main() {
  console.log("** START **\n");

  const propsList = [
    ["a", 11],
    ["b", 22],
  ];

  const obj1 = Object.fromEntries(propsList);

  console.log(obj1);

  console.log("\n** END **");
}

main();
