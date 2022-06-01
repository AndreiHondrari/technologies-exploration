"use strict";

function main() {
  console.log("** START **\n");

  function f1() {
    console.log("THIS", this);
  }

  const f2 = f1.bind(1234);

  f2();

  console.log("\n** END **");
}

main();
