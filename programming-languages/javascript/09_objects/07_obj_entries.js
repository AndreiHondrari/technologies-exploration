"use strict";

function main() {
  console.log("** START **\n");

  const obj1 = {
    a: 11,
    b: 22,
  };

  for (const [x, y] of Object.entries(obj1)) {
    console.log(x, y);
  }

  console.log("\n** END **");
}

main();
