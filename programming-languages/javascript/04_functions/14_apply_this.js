"use strict";

function main() {
  console.log("** START **\n");

  function f1(...args) {
    console.log("THIS", this);
    console.log("ARGS", args);
  }

  /*
  Notice we are sending extra parameters as an array
  */
  f1.apply(111, ["kek", "lol"]);
  f1.apply(222, ["jeff", "pop"]);

  console.log("\n** END **");
}

main();
