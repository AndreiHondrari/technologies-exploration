"use strict";

function main() {
  console.log("** START **\n");

  function f1(...args) {
    console.log("THIS", this);
    console.log("ARGS", args);
  }

  /*
  Notice we are sending extra parameters directly (compared to apply as array)
  */
  f1.call(111, "kek", "lol");
  f1.call(222, "jeff", "pop");

  console.log("\n** END **");
}

main();
