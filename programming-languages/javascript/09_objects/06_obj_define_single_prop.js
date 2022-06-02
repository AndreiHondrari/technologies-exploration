"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = {
    a: 11,
    b: 22,
  };

  Object.defineProperty(obj1, "c", { value: 33, enumerable: true });
  console.log("OBJ AFTER NEW PROPS |", obj1);

  console.log("\n** END **");
}

main();
