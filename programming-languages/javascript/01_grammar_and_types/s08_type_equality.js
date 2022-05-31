"use strict";

function main() {
  console.log("** START **\n");

  const x = "11";

  if (x == 11) { // notice TWO equal signs
    console.log('A | String "11" seems to be equal to the number 11');
  }

  if (x === 11) { // notice THREE equal signs
    console.log('B | "11" still seems to be equal to 11');
  } else {
    console.log('C | at last "11" is definitely not equal to 11 by type');
  }

  if (x === "11") {
    console.log('D | We definitely have a string "11"');
  }

  console.log("\n** END **");
}

main();
