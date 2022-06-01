"use strict";

function main() {
  console.log("** START **\n");

  (function () {
    console.log("Calling self ...");
  })();

  console.log("\n** END **");
}

main();
