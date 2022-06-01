"use strict";

function main() {
  console.log("** START **\n");

  let a = 7 % 2;
  console.log("Remainder/modulo......... |", a);

  let b = 5;
  console.log("Pre - increment.......... |", ++b);
  console.log("Post - increment......... |", b++);
  console.log("..........................|", b);

  let c = 5;
  console.log("Pre - decrement.......... |", --c);
  console.log("Post - decrement......... |", c--);
  console.log("..........................|", c);

  let d = 7 ** 3;
  console.log("Exponentiation........... |", d);

  console.log("\n** END **");
}

main();
