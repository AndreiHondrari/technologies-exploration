"use strict";

/*
It is advised to use let instead of var because it is contained in scope.
*/

function main() {
  console.log("** START **");

  // isolated scope for x
  {
    var x = 11;
  }

  // isolated scope for y
  {
    let y = 22;
  }

  /*
  x is visible outside of scope due to 'var'
  */
  console.log(`X | ${x}`);

  /*
  y will not be visible here because it is outside of scope, due to 'let'.
  */
  try {
    console.log(`Y | ${y}`);
  } catch (e) {
    if (e instanceof ReferenceError) {
      console.log(
        "-> Intentional exception caught | Y not accessible outside of scope",
      );
    } else {
      console.log(Object.getPrototypeOf(e));
    }
  }

  console.log("** END **");
}

main();
