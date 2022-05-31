"use strict";

function main() {
  console.log("** START **\n");

  const x = 777;

  if (x > 10) {
    console.log("x is bigger");
  } else {
    console.log("x is super small");
  }

  if (x > 100 && x < 500) {
    console.log("Oh? centenar!");
  } else if (x >= 500) {
    console.log("oh several hundreds!");
  }

  if (x > 9000) {
    console.log("IT IS OVER 9000 !!!!");
  } else {
    console.log("Disappointing ...not over 9000. So easy to kill!");
  }

  console.log("\n** END **");
}

main();
