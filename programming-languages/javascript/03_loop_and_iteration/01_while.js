"use strict";

function main() {
  console.log("** START **\n");

  // do..while
  let i = 3;
  do {
    console.log("DO WHILE | ", i);
    --i;
  } while (i > 0);

  console.log();

  // regular while
  let j = 0;
  while (j < 3) {
    console.log("WHILE |", j);
    j += 1;
  }

  console.log("\n** END **");
}

main();
