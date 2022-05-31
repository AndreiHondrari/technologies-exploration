"use strict";

function main() {
  console.log("** START **");

  // define a null variable
  let x = null;

  // check if undefined
  if (x === undefined) {
    console.error("X IS UNDEFINED !");
  } else {
    console.log("Seems that x is actually defined ... 🧐");
  }

  if (x === null) {
    console.log("Seems to be null 😳");
  } else {
    console.error("X IS NEITHER NULL !");
  }

  console.log("** END **");
}

main();
