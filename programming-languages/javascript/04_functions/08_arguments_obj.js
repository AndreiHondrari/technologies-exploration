"use strict";

function main() {
  console.log("** START **\n");

  function doSome() {
    console.log("Your arguments are:", arguments);
  }

  doSome(11, 22, 33);

  console.log("\n** END **");
}

main();
