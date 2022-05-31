"use strict";

function main() {
  console.log("** START **");

  // declare undefined variable
  let x;

  // print the undefined variable value (will be undefined ofc)
  console.log(x);

  // check the undefined nature of the variable
  if (x === undefined) {
    console.error("X IS UNDEFINED !");
  }

  // old way of checking undefined nature of variable
  if (typeof (x) === "undefined") {
    console.error("X IS UNDEFINED BY THE OLD WAY!");
  }

  console.log("** END **");
}

main();
