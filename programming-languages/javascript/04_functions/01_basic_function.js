"use strict";

function main() {
  console.log("** START **\n");

  // define a function
  function doThis() {
    console.log("Doing THIS ...");
  }

  // call it
  console.log("Call A");
  doThis();

  // assign the function to a variable or constant
  let f1 = doThis;

  // call the function variable
  console.log("Call B");
  f1();

  console.log("\n** END **");
}

main();
