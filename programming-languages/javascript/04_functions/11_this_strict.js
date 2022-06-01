"use strict";

function main() {
  console.log("** START **\n");

  function f1() {
    console.log("THIS", this);
  }

  f1();

  console.log("\n** END **");
}

main();
