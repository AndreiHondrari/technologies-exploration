"use strict";

function main() {
  console.log("** START **");

  const x = 11;

  try {
    x = 22;
  } catch (e) {
    if (e instanceof TypeError) {
      console.log("Intentionally caught error when changing a constant");
    } else {
      console.error("No error?!");
    }
  }

  console.log("** END **");
}

main();
