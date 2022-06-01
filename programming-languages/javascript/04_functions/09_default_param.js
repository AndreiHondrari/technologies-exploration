"use strict";

function main() {
  console.log("** START **\n");

  function doSome(x, y = 333) {
    console.log("DO_SOME", x, y);
  }

  doSome();
  doSome(11);
  doSome(11, 22);

  console.log("\n** END **");
}

main();
