"use strict";

function main() {
  console.log("** START **\n");

  function f1(val) {
    console.log("Calling F1 with", val);
    return val * 111;
  }

  const doThis = () => f1(7);

  const x = doThis();
  console.log("OUT", x);

  console.log("\n** END **");
}

main();
